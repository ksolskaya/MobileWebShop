#import selenium
import os
from selenium import webdriver
from time import sleep


PHONE_TITLE = 'Samsung Galaxy S5 abonnement'
GENDER = 'Female'
FIRST_NAME = 'Bob'
LAST_NAME = 'Smith'
INITIALS = 'BDB'
DAY = '04'
MONTH = '03'
YEAR = '1995'
CITY = 'Kiev'
POST_CODE = '1111aa'
HOUSE = "4"
TELEPHONE = '0612365478'
EMAIL = 'katherine.solskaya@tele2.com'



chromedriver = 'c:\dev\webdrivers\chromedriver'
#selenium.webdriver.Firefox()
os.environ['webdriver.chrome.driver'] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.maximize_window()
#driver = webdriver.Firefox()
driver.get('http://espresso-3g-uat.tele2.nl:11111/shop/')

#driver.switch_to.frame('frame')
driver.switch_to.frame(driver.find_elements_by_tag_name('iframe')).get()
