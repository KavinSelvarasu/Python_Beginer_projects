import os
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
search_url = 'https://atdigitals.com/about.php'
page_result = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/img")


