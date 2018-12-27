import urllib.request
from urllib.request import urlretrieve
import urllib
from selenium import webdriver
import os
import time
from selenium.common.exceptions import NoSuchElementException

from .settings import Settings

class Util:

    def check_if_private_profile(username):

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        location = Settings.chromedriver_location
        driver = webdriver.Chrome(chrome_options=options, executable_path=location)

        driver.get('https://www.instagram.com/{}/'.format(username))

        try:

            if driver.find_element_by_xpath("//div[@class='QlxVY']"):

                return True
                driver.close()

        except NoSuchElementException:

            return False
            driver.close()

        driver.close()

    def check_if_empty_profile(username):

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        location = Settings.chromedriver_location
        driver = webdriver.Chrome(chrome_options=options, executable_path=location)

        driver.get('https://www.instagram.com/{}/'.format(username))

        try:
            if driver.find_element_by_xpath("//div[@class='coreSpriteProfileCamera']").is_displayed():

                return True
                driver.close()

        except NoSuchElementException:

            return False
            driver.close()

        driver.close()
