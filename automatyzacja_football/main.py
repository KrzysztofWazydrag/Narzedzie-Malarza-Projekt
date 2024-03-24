# pip install selenium beautifulsoup4 webdriver-manager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_argument("--ignore-certificate-errors")
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ['enable-logging'])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.footballcritic.com/serie-a/season-2023-2024/matches/8/68734")

modal = WebDriverWait(driver,50).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'qc-cmp2-footer')]//button[(@mode='primary']"))
)

button_element = driver.find_element(By.XPATH, "//div[contains(@class, 'qc-cmp2-footer')]//button[(@mode='primary']")
button_element.click()
