from pages.multimedia_page import MultimediaPage
from pages.login_page import LoginPage
from pages.base_page import BasePage
from utils.evidence_builder import collector
from utils.screenshot_manager import take_screenshot
from config.config import Config

def test_multimedia_content(driver):
    """Ejemplo: login con credenciales correctas."""
    collector.start_test("Multimedia - Multimedia Validation")
    try:
        base = BasePage(driver)
        driver.get("https://qalab.invertebrado.co/screens/multimedia")

        multimedia = MultimediaPage(driver)
        login = LoginPage(driver)

        # Navegar a login
        assert login.is_element_visible(login.LOGO), "Carga de pagina de login"
        collector.add_step("Pagina de Login visible", "PASS", take_screenshot(driver))

        # Realizar login
        login.login(Config.TEST_USER_NAME, Config.TEST_USER_PASSWORD)

        # Validar login
        multimedia.wait_for_element(multimedia.TITLE)
        multimedia.wait_for_element(multimedia.ELEMENTS)

        assert multimedia.is_element_visible(multimedia.TITLE), "Multimedia content visible"
        collector.add_step("Multimedia", "PASS", take_screenshot(driver))

        assert multimedia.is_element_visible(multimedia.ELEMENTS), "Multimedia elements visible"
        collector.add_step("Multimedia", "PASS", take_screenshot(driver))

        multimedia.get_text(multimedia.ELEMENTS_ID)
        multimedia.get_text(multimedia.ELEMENTS_WEIGHT)
        multimedia.get_text(multimedia.ELEMENTS_DESCRIPTION)
        multimedia.get_src(multimedia.ELEMENTS_PREVIEW)

        collector.add_step("Multimedia content validated", "PASS", take_screenshot(driver))

        driver.implicitly_wait(10)
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