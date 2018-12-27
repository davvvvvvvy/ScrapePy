from selenium import webdriver
from .settings import Settings
from selenium import webdriver

class SetDriver:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.location = Settings.chromedriver_location
        self.driver = webdriver.Chrome(chrome_options=self.options, executable_path=self.location)
        #self.driver = webdriver.Chrome(self.location)
