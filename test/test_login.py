from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.evidence_builder import collector
from utils.screenshot_manager import take_screenshot
from config.config import Config


def test_login_exitoso(driver):
    """Ejemplo: login con credenciales correctas."""
    collector.start_test("Login - Credenciales Correctas")
    try:
        home = HomePage(driver)
        login = LoginPage(driver)

        # Navegar a login
        home.go_to_login()
        collector.add_step("Navegar a Login", "PASS")

        # Verificar que estamos en la pagina de login
        assert login.is_title_visible(), "No se cargo la pagina de login"
        collector.add_step("Pagina de login visible", "PASS", take_screenshot(driver))

        # Realizar login
        login.login(Config.TEST_USER_EMAIL, Config.TEST_USER_PASSWORD)

        # Validar que no hay error
        assert not login.is_error_visible(), "Error: credenciales incorrectas"
        collector.add_step("Login exitoso", "PASS", take_screenshot(driver))

        collector.end_test()

    except Exception as e:
        collector.add_step(str(e), "FAIL", take_screenshot(driver))
        collector.end_test()
        raise


def test_login_credenciales_invalidas(driver):
    """Ejemplo: login con credenciales incorrectas debe mostrar error."""
    collector.start_test("Login - Credenciales Invalidas")
    try:
        home = HomePage(driver)
        login = LoginPage(driver)

        home.go_to_login()
        collector.add_step("Navegar a Login", "PASS")

        login.login("fake@email.com", "wrongpassword")

        assert login.is_error_visible(), "Deberia mostrar mensaje de error"
        collector.add_step("Mensaje de error visible", "PASS", take_screenshot(driver))

        collector.end_test()

    except Exception as e:
        collector.add_step(str(e), "FAIL", take_screenshot(driver))
        collector.end_test()
        raise
