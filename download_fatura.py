from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

from enviroments import NUMERO_NOTA, PASSWORD, USERNAME
from prepare_enviroment import prepare_enviroment

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_experimental_option(
    "prefs",
    {
        "download.default_directory": prepare_enviroment(),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "profile.default_content_settings.popups": 0,
        "plugins.always_open_pdf_externally": True,
    },
)
driver = webdriver.Chrome(options=chrome_options)
wait_driver = WebDriverWait(driver, 10)

# Acessar o site
driver.get("https://nfe-web.portoalegre.rs.gov.br/nfse/")

if driver.find_element(By.CSS_SELECTOR, ".modal.open"):
    driver.find_element(By.CSS_SELECTOR, ".modal-close.modal-exit").click()
    wait_driver.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                '//a[@href="/nfse/pages/security/login.jsf" and @title="Autenticação"]',
            )
        )
    ).click()

    time.sleep(4)

# Preencher o login
driver.find_element(By.ID, "username").send_keys(USERNAME)
driver.find_element(By.ID, "password").send_keys(PASSWORD)
driver.find_element(By.NAME, "envia").click()

time.sleep(4)

menu = wait_driver.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//div[contains(@class, "itemMenu") and @onclick="itemMenuClicked(this)"]',
        )
    )
)

menu.click()

consulta_prestador = wait_driver.until(
    EC.element_to_be_clickable(
        (By.XPATH, '//a[contains(text(), "Consulta do Prestador")]')
    )
)
consulta_prestador.click()

time.sleep(4)

driver.find_element(By.ID, "form:numeroNfsE").send_keys(NUMERO_NOTA)
driver.find_element(By.ID, "form:bt_procurar_NFS-e").click()

time.sleep(4)

driver.find_element(By.ID, "form:j_id160:listaNotas:0:bt_download").click()

time.sleep(2)
