#import selenium
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


PHONE_TITLE = 'LG G3'
GENDER = 'Female'
FIRST_NAME = 'Bob'
LAST_NAME = 'Smith'
INITIALS = 'BDB'
DAY = '05'
MONTH = '02'
YEAR = '1995'
CITY = 'Kiev'
POST_CODE = '1111aa'
HOUSE = "4"
TELEPHONE = '0612365478'
EMAIL = 'katherine.solskaya@tele2.com'
IBAN = 'NL27ABNA0505526050'
ID = 'PASSPORT'
ID_CARD = 'IMF22D3K1'
DELIVERY = 'Ander punt kiezen'
LINK_NAME = 'Ander punt kiezen'

#accept_button = [By.ID, 'buttonAccept']
#driver.find_element(accept_button[0], accept_button[1])

chromedriver = 'c:\dev\webdrivers\chromedriver'
#selenium.webdriver.Firefox()
os.environ['webdriver.chrome.driver'] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.maximize_window()
#driver = webdriver.Firefox()
driver.get('http://espresso-3g-uat.tele2.nl:11111/shop/')

# Handle iframe
iframe = driver.find_element_by_id('qb_cookie_consent_main')
driver.switch_to.frame(iframe)
driver.find_element_by_id('buttonAccept').click()
driver.switch_to.default_content()


elements = driver.find_elements_by_class_name('fld_title')
for el in elements:
    if el.text == PHONE_TITLE:
        el.click()
        break
sleep(3)

driver.find_element_by_class_name('btn_with_icon').click()
sleep(3)

driver.find_element_by_id('genderSelectBoxIt').click()
sleep(3)
ul = driver.find_element_by_id('genderSelectBoxItOptions')
lis = ul.find_elements_by_tag_name('li')
for li in lis:
    if li.get_attribute('data-val') == GENDER:
        li.click()
        break
sleep(3)
driver.find_element_by_id('firstname').send_keys(FIRST_NAME)
driver.find_element_by_id('lastname').send_keys(LAST_NAME)
driver.find_element_by_id('initials').send_keys(INITIALS)
sleep(3)

driver.find_element_by_id('daySelectBoxIt').click()
sleep(3)
ul = driver.find_element_by_id('daySelectBoxItOptions')
lis = ul.find_elements_by_tag_name('li')
for li in lis:
    if li.get_attribute('data-val') == DAY:
        li.click()
        break

driver.find_element_by_id('monthSelectBoxIt').click()
sleep(3)
ul = driver.find_element_by_id('monthSelectBoxItOptions')
lis = ul.find_elements_by_tag_name('li')
for li in lis:
    if li.get_attribute('data-val') == MONTH:
        li.click()
        break

driver.find_element_by_id('yearSelectBoxIt').click()
sleep(2)
ul=driver.find_element_by_id('yearSelectBoxItOptions')
lis = ul.find_elements_by_tag_name('li')
for li in lis:
    if li.get_attribute('data-val') == YEAR:
        li.click()
        break

driver.find_element_by_id('placeofbirth').send_keys(CITY)
driver.find_element_by_id('postcode').send_keys(POST_CODE)
driver.find_element_by_id('house').send_keys(HOUSE)
driver.find_element_by_id('telephone').send_keys(TELEPHONE)
driver.find_element_by_id('e-mail').send_keys(EMAIL)
driver.find_element_by_id('repeat-email').send_keys(EMAIL)
driver.find_element_by_id('btn_step_one next-step-1').click()
#govnocod
sleep(3)
driver.find_element_by_class_name('icon').click()
driver.find_element_by_id('btn_step_one next-step-1').click()
sleep(1)

loader_displayed = True
while loader_displayed:
    loader_displayed = driver.find_element_by_class_name("spinner-info").is_displayed()
    sleep(1)


driver.find_element_by_id('rekeningnummer').send_keys(IBAN)
sleep(2)

driver.find_element_by_id('identificationSelectBoxIt').click()
sleep(2)
ul=driver.find_element_by_id('identificationSelectBoxItOptions')
lis = ul.find_elements_by_tag_name('li')
for li in lis:
    if li.get_attribute('data-val') == ID:
        li.click()
        break

driver.find_element_by_id('docnumber').send_keys(ID_CARD)

driver.find_element_by_id('btn_step_two next-step-2').click()
sleep(3)

driver.find_element_by_css_selector('i.checkbox-ico').click()
sleep(3)

# Agree with Terms and Conditions
driver.find_element_by_id('terms-1-container').click()
driver.find_element_by_id('terms-2-container').click()

driver.find_element_by_id('btn_step_three next-step-3').click()

