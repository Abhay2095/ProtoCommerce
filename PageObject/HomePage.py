from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select


class HomePage:
    txt_name_name = "name"
    txt_email_name = "email"
    ch_box_id = "exampleCheck1"
    drp_gender_xpath = "//select[@id='exampleFormControlSelect1']"
    btn_submit_xpath = "//input[@value='Submit']"
    shop_xpath = "//a[normalize-space()='Shop']"

    def __init__(self, driver):
        self.driver = driver

    def setname(self, name):
        self.driver.find_element(By.NAME, self.txt_name_name).send_keys(name)

    def setmail(self, email):
        self.driver.find_element(By.NAME, self.txt_email_name).send_keys(email)

    def clickchbox(self):
        self.driver.find_element(By.ID, self.ch_box_id).click()

    def setgender(self, gender):
        tp = self.driver.find_element(By.XPATH, self.drp_gender_xpath)
        drp = Select(tp)
        return drp.select_by_visible_text(gender)

    def clicksubmit(self):
        self.driver.find_element(By.XPATH, self.btn_submit_xpath).click()

    def clickonshop(self):
        self.driver.find_element(By.XPATH, self.shop_xpath).click()


























