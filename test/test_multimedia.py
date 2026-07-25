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

        assert multimedia.is_element_visible(multimedia.TITLE), "Multimedia content visible"
        multimedia.wait_for_element(multimedia.ELEMENTS)
        
        assert multimedia.is_element_visible(multimedia.ELEMENTS), "Multimedia elements visible"
        collector.add_step("Multimedia", "PASS", take_screenshot(driver))
        
        id = multimedia.get_text(multimedia.ELEMENTS_ID)
        weight = multimedia.get_text(multimedia.ELEMENTS_WEIGHT)
        description = multimedia.get_text(multimedia.ELEMENTS_DESCRIPTION)
        preview_src = multimedia.get_src(multimedia.ELEMENTS_PREVIEW)

        collector.add_step("ID: " + id, "PASS")
        collector.add_step("Weight: " + weight, "PASS")
        collector.add_step("Description: " + description, "PASS")
        collector.add_step("Preview Src: " + preview_src, "PASS")
        collector.add_step("Preview: <br><img class='img-preview' src='" + preview_src + "'>", "PASS")

        collector.end_test()

    except Exception as e:
        collector.add_step(str(e), "FAIL", take_screenshot(driver))
        collector.end_test()
        raise
