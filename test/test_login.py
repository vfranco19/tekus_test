from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.base_page import BasePage
from utils.evidence_builder import collector
from utils.screenshot_manager import take_screenshot
from config.config import Config


def test_login_exitoso(driver):
    """Ejemplo: login con credenciales correctas."""
    collector.start_test("Login - Credenciales Correctas")
    try:
        base = BasePage(driver)
        home = HomePage(driver)
        login = LoginPage(driver)

        # Navegar a login
        assert login.is_element_visible(login.LOGO), "Carga de pagina de login"
        collector.add_step("Pagina de Login visible", "PASS", take_screenshot(driver))

        # Realizar login
        login.login(Config.TEST_USER_NAME, Config.TEST_USER_PASSWORD)
        assert login.is_element_visible(login.LOGIN_BUTTON), "Login button visible"
        collector.add_step("Formulario de login diligenciado", "PASS", take_screenshot(driver))

        if login.is_warning_visible():
            collector.add_step("Warning visible", "WARNING", take_screenshot(driver))
            print("Warning visible: ", login.get_text(login.WARNING_MESSAGE))
        #driver.implicitly_wait(10)  # Espera para que se procese el login
        # Validar que no hay error

        assert login.is_element_visible(login.TITLE), "Inicio de sesion exitoso, titulo visible"
        collector.add_step("Login exitoso", "PASS", take_screenshot(driver))

        collector.end_test()

    except Exception as e:
        collector.add_step(str(e), "FAIL", take_screenshot(driver))
        collector.end_test()
        raise

'''
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
'''