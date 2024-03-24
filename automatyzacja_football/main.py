from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service



options = Options()
options.add_argument("--ignore-certificate-errors")
options.add_experimental_option(name:"detach", value:True)
options.add_experimental_option(name:"excludeSwitches", value:['enable-logging'])
