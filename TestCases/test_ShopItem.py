import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Utilities.ReadProperties import ReadConfig
from PageObject.ShopItem import ShopItem
from PageObject.HomePage import HomePage


class Test_ShopItem:
    baseurl = ReadConfig.geturl()
    location = ReadConfig.getlocation()

    def test_shopitem(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(15)
        self.hp = HomePage(self.driver)
        self.hp.clickonshop()

        self.si = ShopItem(self.driver)
        self.si.card_title()
        self.si.clickoncheckout()
        self.si.clickonfinalcheckout()
        self.si.setlocation(self.location)
        self.si.clickonpurchase()

        self.msg = self.driver.find_element(By.XPATH , "//strong[normalize-space()='Success!']").text

        if 'Success!' in self.msg:
            assert True
        else:
            assert False

