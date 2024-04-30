import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObject.HomePage import HomePage
from Utilities.ReadProperties import ReadConfig


class Test_homepage:

    baseurl = ReadConfig.geturl()
    name = ReadConfig.getname()
    email = ReadConfig.getemail()


    def test_homepage_succesfully(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(15)
        self.hp = HomePage(self.driver)
        self.hp.setname(self.name)
        self.hp.setmail(self.email)
        self.hp.clickchbox()
        self.hp.setgender('Female')
        self.hp.clicksubmit()

        self.msg = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text

        if 'Success!' in self.msg:
            assert True

        else:
            assert False

































