from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MultimediaPage(BasePage):
    """Page Object de la pagina principal."""

    # ── Localizadores ─────────────────────────────────────────────────
    NAV_MULTIMEDIA = (By.XPATH, "//a[@href='/screens/multimedia']/parent::div")
    TITLE = (By.XPATH, "//h1[text()='Multimedia']")
    ELEMENTS = (By.XPATH, "//div[@class='col ark-card-information-content'][1]")
    ELEMENTS_ID = (By.XPATH, "//span[@class='ark-card-content-id'][1]")
    ELEMENTS_WEIGHT = (By.XPATH, "//span[@class='ark-size-file'][1]")
    ELEMENTS_DESCRIPTION = (By.XPATH, "//a[contains(@class,'ark-card-title')][1]")
    ELEMENTS_PREVIEW = (By.XPATH, "//img[@class='ark-img-preview img-fluid'][1]")
    # ── Acciones ──────────────────────────────────────────────────────
