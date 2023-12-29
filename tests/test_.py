import pdb

from tests.Locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from tests.generate_test import GenerateEmailPassword

se = Service(executable_path='C:/Users/nataliian/Downloads/chromedriver-win32/chromedriver.exe')
driver = webdriver.Chrome(service=se)
driver.get('http://demostore.supersqa.com/my-account/')
pdb.set_trace()


class FindAndClick(GenerateEmailPassword):

    def __init__(self, driver):
        self.driver = driver
        self.def_timeout = 30
        self.lc = Locators

    def timeout_wait_input(self, text, timeout=None):
        timeout = timeout if timeout else self.def_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.lc.field_email)).send_keys(text)

    def timeout_wait_click(self, timeout=None):
        timeout = timeout if timeout else self.def_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.lc.register_btn)).click()

