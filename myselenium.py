from selenium import webdriver
from selenium.webdriver.common.keys import Keys

base_url = "https://kea-fronter.itslearning.com/"

username = "abdu0445"

driver=webdriver.Chrome(executable_path="C:/Users/slmns/Downloads/Drivers/chromedriver.exe")

driver.maximize_window()

driver.implicitly_wait(10)

driver.get(base_url)

login = driver.find_element_by_link_text("Log på med UNI-Login")
login.click()


input_username = driver.find_element_by_id("username")

input_username.clear()
input_username.send_keys(username)

username_button = driver.find_element_by_css_selector(".button")
username_button.click()