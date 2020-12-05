from selenium import webdriver
from time import *

url = 'https://www.youtube.com/'
url1 = 'https://google.co.in/'
driverPath = '/Users/kavinselvaraj/Own_Projects/Python_Beginer_projects/webscraping/chromedriver'


class WebScraping:
    def __init__(self, link):
        self.driver_path = webdriver.Chrome(executable_path=driverPath)
        self.driver_path.get(link)
        # self.xpath = self.driver_path.find_element_by_xpath(
        #     '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/paper-button')
        # self.xpath.click()
        sleep(3)


WebScraping(url1)
