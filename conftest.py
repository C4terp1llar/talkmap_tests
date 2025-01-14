import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import requests

@pytest.fixture(scope="session")
def browser():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    yield driver
    driver.quit()


@pytest.fixture
def login(browser):
    browser.get("http://localhost:5173/login")

    email_field = browser.find_element(By.ID, "login__email")
    assert email_field.is_displayed(), "Поле для ввода email не отображается"

    password_field = browser.find_element(By.ID, "login__password")
    assert password_field.is_displayed(), "Поле для ввода пароля не отображается"

    login_button = browser.find_element(By.ID, "login__enter-btn")
    assert login_button.is_displayed(), "Кнопка 'Войти' не отображается"

    email_field.send_keys("m0skvitin@mail.ru")
    password_field.send_keys("123qwe")

    login_button = browser.find_element(By.ID, "login__enter-btn")
    login_button.click()

    WebDriverWait(browser, 5).until(
        EC.url_to_be("http://localhost:5173/app/home")
    )

    assert browser.current_url == "http://localhost:5173/app/home", "После входа c корректными данными не перенаправляет на страницу профиля"


BASE_URL = "http://localhost:5000/api"

@pytest.fixture(scope="session")
def api_client():
    class APIClient:
        def __init__(self, base_url):
            self.base_url = base_url

        def post(self, endpoint, data, headers=None):
            return requests.post(f"{self.base_url}{endpoint}", json=data, headers=headers)

    return APIClient(BASE_URL)

