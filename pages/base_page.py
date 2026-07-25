from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
)
from utils.logger import logger
from config.config import Config


class BasePage:
    """Clase base con metodos comunes para todas las paginas.

    Todas las Page Objects deben heredar de esta clase.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.TIMEOUT)

    # ── Wait & Visibility ─────────────────────────────────────────────

    def wait_for_element(self, locator):
        """Espera a que un elemento sea visible y lo retorna."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_element_visible(self, locator):
        """Retorna True si el elemento es visible, False si no."""
        try:
            self.wait_for_element(locator)
            return True
        except TimeoutException:
            return False

    # ── Actions ───────────────────────────────────────────────────────

    def click(self, locator):
        """Hace click en un elemento despues de esperarlo."""
        element = self.wait_for_element(locator)
        element.click()

    def safe_click(self, locator):
        """Click seguro: scroll al elemento + fallback con JS si falla."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", element
        )
        try:
            element.click()
        except (ElementClickInterceptedException, NoSuchElementException):
            self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, locator, text):
        """Limpia un campo y escribe texto."""
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Retorna el texto de un elemento."""
        element = self.wait_for_element(locator)
        return element.text

    def get_src(self, locator):
        """Retorna el atributo src de un elemento."""
        element = self.wait_for_element(locator)
        return element.get_attribute("src")

    # ── Overlays / Ads (opcional) ─────────────────────────────────────

    def remove_overlays(self):
        """Elimina overlays fijos que puedan bloquear clicks."""
        self.driver.execute_script("""
            document.querySelectorAll('iframe, div, section').forEach(el => {
                const style = window.getComputedStyle(el);
                if (style.position === 'fixed' && parseInt(style.zIndex) > 999) {
                    el.remove();
                }
            });
        """)

    def remove_ads_iframes(self):
        """Elimina iframes de publicidad."""
        self.driver.execute_script("""
            document.querySelectorAll("iframe").forEach(iframe => {
                if (iframe.src.includes("googleads") ||
                    iframe.src.includes("doubleclick") ||
                    iframe.id.includes("aswift")) {
                    iframe.remove();
                }
            });
        """)
