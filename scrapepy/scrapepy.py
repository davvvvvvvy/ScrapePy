import urllib.request
from urllib.request import urlretrieve
import urllib
from selenium import webdriver
import os
import time
from selenium.common.exceptions import NoSuchElementException
from tqdm import tqdm

from .settings import Settings
from .util import Util

class ScrapePy:

    def __init__(self):

        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.location = Settings.chromedriver_location
        self.driver = webdriver.Chrome(chrome_options=self.options, executable_path=self.location)

    def scrape_by_username(self, username):

        url = 'https://www.instagram.com/{}/'.format(username)

        driver = self.driver
        driver.get(url)

        if driver.find_elements_by_xpath("//div[@class='error-container']"):
            print(" >>> Wrong url!")

        elif Util.check_if_empty_profile(username) == True:
            print(" >>> Account doesn't have any post!")

        elif Util.check_if_private_profile(username) == True:
            print(" >>> Account is private!")

        else:

            try:

                srcs = []

                for i in range(1, 7):
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(2)

                    img = driver.find_elements_by_tag_name('a')
                        #'//img[@class="FFVAD"]')'''

                    src = [s.get_attribute('href') for s in img if '.com/p/' in s.get_attribute('href')]
                    [srcs.append(href) for href in src if href not in srcs]

            except NoSuchElementException:

                print(" >>> Can't find element!")

            src_col = []
            i=0
            for sr in srcs:
                i+=1
                driver.get(sr)
                print("\n >>> Collecting {}/{}, -> {}".format(i, len(srcs), sr))
                time.sleep(2)

                try:
                    a = driver.find_element_by_xpath('//img[@class="FFVAD"]').get_attribute('src')
                    print(" >>> Collected!")
                    src_col.append(a)

                except NoSuchElementException:

                    print(" >>> Can't find this element!")

            print(src_col)

            num = 1
            for srces in src_col:

                try:
                    '''for i in tqdm(range(len(src_col))):
                        urllib.request.urlretrieve(srces, '{}.jpg'.format(num))
                        print(" >>> Downloaded {}/{})".format(num, len(src_col)))
                        num+=1'''

                    for f in tqdm(range(10), ascii=True, desc="  >>> Downloading"):
                        pass

                    urllib.request.urlretrieve(srces, '{}.jpg'.format(num))
                    print(" >>> Downloaded {}/{}".format(num, len(src_col)))
                    num+=1

                except Exception as e:
                    time.sleep(2)
                    print(" >>> Can't download, don't know, don't care")

        driver.close()


    def scrape_by_hashtag(self, hashtag):

        url = 'https://www.instagram.com/explore/tags/{}/'.format(hashtag)

        driver = self.driver
        driver.get(url)

        if driver.find_elements_by_xpath("//div[@class='error-container']"):
            print(" >>> Wrong url!")

        elif Util.check_if_empty_profile(username) == True:
            print(" >>> Account doesn't have any post!")

        elif Util.check_if_private_profile(username) == True:
            print(" >>> Account is private!")

        else:

            try:

                srcs = []

                for i in range(1, 7):
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(2)

                    img = driver.find_elements_by_tag_name('a')
                        #'//img[@class="FFVAD"]')'''

                    src = [s.get_attribute('href') for s in img if '.com/p/' in s.get_attribute('href')]
                    [srcs.append(href) for href in src if href not in srcs]

            except NoSuchElementException:

                print(" >>> Can't find element!")

            src_col = []
            i=0
            for sr in srcs:
                i+=1
                driver.get(sr)
                print("\n >>> Collecting {}/{}, -> {}".format(i, len(srcs), sr))
                time.sleep(2)

                try:
                    a = driver.find_element_by_xpath('//img[@class="FFVAD"]').get_attribute('src')
                    print(" >>> Collected!")
                    src_col.append(a)

                except NoSuchElementException:

                    print(" >>> Can't find this element!")

            print(src_col)

            num = 1
            for srces in src_col:

                try:

                    for f in tqdm(range(10), ascii=True, desc="  >>> Downloading"):
                        pass

                    urllib.request.urlretrieve(srces, '{}.jpg'.format(num))
                    print(" >>> Downloaded {}/{}".format(num, len(src_col)))
                    num+=1

                except Exception as e:
                    time.sleep(2)
                    print(" >>> Can't download, don't know, don't care")

        driver.close()

    def scrape_videos_by_username(self, username):

        url = 'https://www.instagram.com/{}/'.format(username)

        driver = self.driver
        driver.get(url)

        if driver.find_elements_by_xpath("//div[@class='error-container']"):
            print(" >>> Wrong url!")

        elif Util.check_if_empty_profile(username) == True:
            print(" >>> Account doesn't have any post!")

        elif Util.check_if_private_profile(username) == True:
            print(" >>> Account is private!")

        else:

            try:

                srcs = []

                for i in range(1, 7):
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(2)

                    img = driver.find_elements_by_tag_name('a')
                        #'//img[@class="FFVAD"]')'''

                    src = [s.get_attribute('href') for s in img if '.com/p/' in s.get_attribute('href')]
                    [srcs.append(href) for href in src if href not in srcs]

            except NoSuchElementException:

                print(" >>> Can't find element!")

            src_col = []
            i=0
            for sr in srcs:
                i+=1
                driver.get(sr)
                print("\n >>> Collecting {}/{}, -> {}".format(i, len(srcs), sr))
                time.sleep(2)

                try:
                    a = driver.find_element_by_xpath('//video[@class="tWeCl"]').get_attribute('src')
                    print(" >>> Collected!")
                    src_col.append(a)

                except NoSuchElementException:

                    print(" >>> Can't find this element!")

            print(src_col)

            num = 1
            for srces in src_col:

                try:

                    for f in tqdm(range(10), ascii=True, desc="  >>> Downloading"):
                        pass

                    urllib.request.urlretrieve(srces, '{}.mp4'.format(num))
                    print(" >>> Downloaded {}/{}".format(num, len(src_col)))
                    num+=1

                except Exception as e:
                    time.sleep(2)
                    print(" >>> Can't download, don't know, don't care")

        driver.close()


    def scrape_videos_by_hashtag(self, hashtag):

        url = 'https://www.instagram.com/explore/tags/{}/'.format(hashtag)

        driver = self.driver
        driver.get(url)

        if driver.find_elements_by_xpath("//div[@class='error-container']"):
            print(" >>> Wrong url!")

        elif Util.check_if_empty_profile(username) == True:
            print(" >>> Account doesn't have any post!")

        elif Util.check_if_private_profile(username) == True:
            print(" >>> Account is private!")

        else:

            try:

                srcs = []

                for i in range(1, 7):
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(2)

                    img = driver.find_elements_by_tag_name('a')
                        #'//img[@class="FFVAD"]')'''

                    src = [s.get_attribute('href') for s in img if '.com/p/' in s.get_attribute('href')]
                    [srcs.append(href) for href in src if href not in srcs]

            except NoSuchElementException:

                print(" >>> Can't find element!")

            src_col = []
            i=0
            for sr in srcs:
                i+=1
                driver.get(sr)
                print("\n >>> Collecting {}/{}, -> {}".format(i, len(srcs), sr))
                time.sleep(2)

                try:
                    a = driver.find_element_by_xpath('//video[@class="tWeCl"]').get_attribute('src')
                    print(" >>> Collected!")
                    src_col.append(a)

                except NoSuchElementException:

                    print(" >>> Can't find this element!")

            print(src_col)

            num = 1
            for srces in src_col:

                try:

                    for f in tqdm(range(10), ascii=True, desc="  >>> Downloading"):
                        pass

                    urllib.request.urlretrieve(srces, '{}.mp4'.format(num))
                    print(" >>> Downloaded {}/{}".format(num, len(src_col)))
                    num+=1

                except Exception as e:
                    time.sleep(2)
                    print(" >>> Can't download, don't know, don't care")

        driver.close()
