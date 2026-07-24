from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    """Page Object de la pagina principal.

    Modifica los localizadores segun tu aplicacion.
    """

    # ── Localizadores ─────────────────────────────────────────────────
    NAV_LOGIN = (By.XPATH, "//a[@href='/login']")
    NAV_CONTACT = (By.XPATH, "//a[@href='/contact_us']")
    LOGO = (By.ID, "logo")

    # ── Acciones ──────────────────────────────────────────────────────

    def go_to_login(self):
        self.safe_click(self.NAV_LOGIN)

    def go_to_contact(self):
        self.safe_click(self.NAV_CONTACT)

    def is_logo_visible(self):
        return self.is_element_visible(self.LOGO)
