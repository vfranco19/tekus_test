from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object de la pagina de login.

    Modifica los localizadores segun tu aplicacion.
    """

    # ── Localizadores ─────────────────────────────────────────────────
    TITLE = (By.XPATH, "//h2[text()='Login to your account']")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='login-email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
    ERROR_MESSAGE = (By.XPATH, "//p[text()='Your email or password is incorrect!']")

    # ── Acciones ──────────────────────────────────────────────────────

    def login(self, email, password):
        """Completa el formulario de login y hace click en submit."""
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        self.safe_click(self.LOGIN_BUTTON)

    def is_title_visible(self):
        return self.is_element_visible(self.TITLE)

    def is_error_visible(self):
        return self.is_element_visible(self.ERROR_MESSAGE)
