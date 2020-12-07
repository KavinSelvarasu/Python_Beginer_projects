from selenium import webdriver
from time import *

url = 'https://www.youtube.com/'
url1 = 'https://google.co.in/'
mediumUrl = 'https://writingcooperative.com/the-exact-software-tools-i-use-to-sell-an-online-writing-course' \
            '-52176a8a97c2 '
driverPath = '/Users/kavinselvaraj/Own_Projects/Python_Beginer_projects/webscraping/chromedriver'


class WebScraping:
    def __init__(self, link):
        self.driver_path = webdriver.Chrome(executable_path=driverPath)
        self.driver_path.get(link)
        self.mediumPara = self.driver_path.find_elements_by_tag_name('p')
        self.x = []
        for obj in self.mediumPara:
            innerData = obj.get_attribute('innerHTML')
            print(innerData)
            # save data to file
            self.f = open('temp2.txt', 'x')
            self.f.write(innerData)
            print(self.f.close())


WebScraping(mediumUrl)
