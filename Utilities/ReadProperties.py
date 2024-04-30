import pytest
from selenium import webdriver

import configparser

config = configparser.RawConfigParser()
config.read("E:\\ProtoCommerce\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def geturl():
        baseurl = config.get('base info', 'baseurl')
        return baseurl

    @staticmethod
    def getname():
        name = config.get('base info', 'name')
        return name

    @staticmethod
    def getemail():
        email = config.get('base info', 'email')
        return email

    @staticmethod
    def getlocation():
        location = config.get('base info', 'location')
        return location


























