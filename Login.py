from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.Locators import Locators
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from test_ import GenerateEmailPassword, FindAndClick
import pdb
# /my-account/
se = Service(executable_path='C:/Users/nataliian/Downloads/chromedriver-win32/chromedriver.exe')
driver = webdriver.Chrome(service=se)

driver = driver.get("http://demostore.supersqa.com/my-account/")
pdb.set_trace()


class Login(Locators):

    def __init__(self, driver):
        self.driver = driver
        self.valid_email = "nataliia.nazarenko@yahoo.com"
        self.valid_pas = "Nataliia31@"
        self.def_timeout = 180

    @staticmethod
    def go_to_my_account():
        driver.get("http://demostore.supersqa.com/my-account/")
        print("0")

    def email_login(self, field_email_login, timeout=None):
        timeout = timeout if timeout else self.def_timeout
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(field_email_login)).send_keys(
            self.valid_email)
        print("1")

    def pas_login(self, field_pas_login, timeout=None):
        timeout = timeout if timeout else self.def_timeout
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(field_pas_login)).send_key(
            self.valid_pas)
        print("2")

    def login_btn(self, login_btn, timeout=None):
        timeout = timeout if timeout else self.def_timeout
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(login_btn)).click()
        print("3")


