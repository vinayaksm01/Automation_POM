class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.logout_link_xpath = "//*[@id='logoutLink']"

    def click_on_logout_link(self):
        self.driver.find_element_by_xpath(self.logout_link_xpath).click()
