import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from utils.evidence_builder import collector
from utils.html_master_report import generate_master_report
from config.config import Config


def pytest_sessionfinish(session, exitstatus):
    """Genera el reporte HTML al finalizar toda la sesion de pytest."""
    json_path = collector.save()
    print(f"\nReporte JSON guardado en: {json_path}")
    generate_master_report(json_path)
    print("Reporte HTML generado en: evidence/reports/execution_report.html")


@pytest.fixture
def driver():
    """Fixture que levanta Chrome, navega a BASE_URL y limpia al finalizar."""
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")

    prefs = {
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.geolocation": 2,
        "profile.default_content_setting_values.popups": 2,
        "profile.managed_default_content_settings.images": 1,
        "profile.managed_default_content_settings.ads": 2,
    }
    options.add_experimental_option("prefs", prefs)

    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(Config.BASE_URL)

    yield driver

    driver.quit()
