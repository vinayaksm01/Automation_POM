import time

import allure
import pytest
import moment
from pages.loginpage import LoginPage
from pages.homepage import HomePage
from utils import constants as data
import os


@pytest.mark.usefixtures("test_setup")
class TestLogin:
    def test_login(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.enter_un(data.UN)
        lp.enter_pwd(data.PWD)
        lp.click_login()

    def test_logout(self):
        try:
            driver = self.driver
            time.sleep(5)
            hp = HomePage(driver)
            hp.click_on_logout_link()

            x = driver.title
            assert x == 'actiTIME - Logi'
        except AssertionError as e:
            print(e)
            cur_time = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            test_name = data.whoami()
            screenshot_name = test_name + "_" + cur_time

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file(
                os.getcwd().replace("\\", "/")+"/screenshots/" + screenshot_name + ".png")
            print(os.getcwd().replace("\\", "/").replace("tests", "screenshots") + "/" + screenshot_name + ".png")
            raise
        except:
            print("there is an exception")
            raise
        else:
            print("No exception block")
        finally:
            print("in finally block")
