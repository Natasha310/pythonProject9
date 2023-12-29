from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
se = Service(executable_path='C:/Users/nataliian/Downloads/chromedriver-win32/chromedriver.exe')
driver = webdriver.Chrome(service=se)


class Locators:

    field_email = (By.ID, 'reg_email')
    field_pas = (By.ID, 'reg_password')
    register_btn = (By.NAME, 'register')
    field_email_login = (By.ID, 'username')
    field_pas_login = (By.ID, 'password')
    login_btn = (By.NAME, 'login')
    checkbox_remember = (By.NAME, 'rememberme')
    link_forgot_pas = (By.CLASS_NAME, 'woocommerce-LostPassword lost_password')
    valid_email = "nataliia.nazarenko@yahoo.com"
    valid_pas = "Nataliia31@"
