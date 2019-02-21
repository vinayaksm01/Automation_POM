class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.un_txt_xpath = "//*[@id='username']"
        self.pwd_txt_xpath = "//*[@name='pwd']"
        self.login_btn_xpath = "//*[text()='Login ']"

    def enter_un(self,un):
        self.driver.find_element_by_xpath(self.un_txt_xpath).send_keys(un)

    def enter_pwd(self, pwd):
            self.driver.find_element_by_xpath(self.pwd_txt_xpath).send_keys(pwd)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_btn_xpath).click()
