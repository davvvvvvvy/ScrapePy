from scrapepy.settings import Settings
from scrapepy.driver import SetDriver
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('headless')
location = Settings.chromedriver_location
driver = webdriver.Chrome(chrome_options=options, executable_path=location)

driver.get("https://google.com")
