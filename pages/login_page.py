from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Page Object de la pagina de login.

    Modifica los localizadores segun tu aplicacion.
    """

    # ── Localizadores ─────────────────────────────────────────────────
    TITLE = (By.XPATH, "//h1[@class='ark-h1']")
    USERNAME_INPUT = (By.XPATH, "//input[@formcontrolname='userName']")
    PASSWORD_INPUT = (By.XPATH, "//input[@formcontrolname='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class,'mat-primary')]")
    ERROR_MESSAGE = (By.XPATH, "//p[text()='Your email or password is incorrect!']")
    WARNING_MESSAGE = (By.XPATH, "//div[@role='alert']")
    LOGO = (By.XPATH, "//div[@class='col ark-form-login-logo-content']")

    # ── Acciones ──────────────────────────────────────────────────────

    def login(self, username, password):
        """Completa el formulario de login y hace click en submit."""
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.safe_click(self.LOGIN_BUTTON)

    def is_title_visible(self):
        return self.is_element_visible(self.TITLE)

    def is_warning_visible(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.WARNING_MESSAGE)
            )
            return True
        except TimeoutException:
            return False

    def is_error_visible(self):
        return self.is_element_visible(self.ERROR_MESSAGE)
