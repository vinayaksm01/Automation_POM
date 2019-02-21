import pytest
import os
from utils import constants as data


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='test help')


@pytest.fixture(scope='class')
def test_setup(request):
    from selenium import webdriver
    cur_dir = os.getcwd().replace("\\", "/")
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=cur_dir + "/drivers/chromedriver.exe")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=cur_dir + "/drivers/geckodriver.exe")
    driver.get(data.URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver = driver
    yield
    driver.quit()
