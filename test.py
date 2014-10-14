#import selenium
import os
from selenium import webdriver

chromedriver = 'c:\dev\webdrivers\chromedriver'
#selenium.webdriver.Firefox()
os.environ['webdriver.chrome.driver'] = chromedriver
chrome = webdriver.Chrome(chromedriver)
#driver = webdriver.Firefox()
chrome.stop_client()