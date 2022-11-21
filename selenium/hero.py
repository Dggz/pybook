from random import randint
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def random_sleep(min_sec, max_sec=None):
    if not max_sec:
        max_sec = min_sec
    sleep(randint(min_sec, max_sec))


# For prod this should probably have multiple browser drivers installed and randomly use one each time
driver = webdriver.Chrome(r"D:\chromedriver")
driver.get("https://hero.uber.com/")
random_sleep(1, 4)

username = driver.find_element_by_name('textInputValue')
username.clear()
username.send_keys("developers@splend.com")
random_sleep(1)
username.send_keys(Keys.RETURN)
random_sleep(3, 7)

password = driver.find_element_by_id('password')
password.clear()
password.send_keys("6he9jwNkKGK7IDH#7AMk")
random_sleep(1)
password.send_keys(Keys.RETURN)
random_sleep(1, 4)


try:
    close_consent = driver.find_element_by_id('cookie-banner-close-button')
    close_consent.click()
    random_sleep(2)
except Exception:
    pass


button = driver.find_element_by_xpath("//*[contains(text(), 'Add driver')]")
button.click()
random_sleep(4)

first_name = driver.find_element_by_id('first-name')
first_name.clear()
first_name.send_keys("First")
random_sleep(2)

last_name = driver.find_element_by_id('last-name')
last_name.clear()
last_name.send_keys("Last")
random_sleep(3, 5)

phone_number = driver.find_element_by_id('phone-number')
phone_number.clear()
number = ''.join([str(randint(0,9)) for i in range(8)])
phone_number.send_keys(f"04{number}")
random_sleep(1, 3)


cbutton = driver.find_element_by_xpath("//*[contains(text(), 'Continue')]")
cbutton.click()
random_sleep(2, 7)

drive_type = driver.find_element_by_xpath("//*[contains(text(), 'Drive with Uber')]")
drive_type.click()
random_sleep(1, 2)

create_driver = driver.find_element_by_xpath("//*[contains(text(), 'Create driver')]")
create_driver.click()

random_sleep(5)
