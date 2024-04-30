import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


class ShopItem:

    card_title_xpath = "(//h4[@class='card-title'])"
    card_footer_xpath = "(//div[@class='card-footer'])"
    checkout_xpath = "//a[@class='nav-link btn btn-primary']"
    final_checkout_xpath = "//button[normalize-space()='Checkout']"
    location_id = "country"
    location_xpath = "//a[normalize-space()='India']"
    purchase_xpath = "//input[@value='Purchase']"

    def __init__(self, driver):
        self.driver = driver

    def card_title(self):
        cards = self.driver.find_elements(By.XPATH, self.card_title_xpath)
        card_footers = self.driver.find_elements(By.XPATH, self.card_footer_xpath)

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            if cardText == 'Blackberry':
                card_footers[i].click()


    def clickoncheckout(self):
        self.driver.find_element(By.XPATH, self.checkout_xpath).click()

    def clickonfinalcheckout(self):
        self.driver.find_element(By.XPATH, self.final_checkout_xpath).click()

    def setlocation(self, location):
        self.driver.find_element(By.ID, self.location_id).send_keys(location)
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.location_xpath).click()

    def clickonpurchase(self):
        self.driver.find_element(By.XPATH, self.purchase_xpath).click()





























