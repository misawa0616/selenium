from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
with webdriver.Chrome() as driver:
    driver.get("http://127.0.0.1:8000/admin/login/")
    driver.find_element(By.NAME, "username").send_keys(
        "admin")
    driver.find_element(By.NAME, "password").send_keys(
        "admin")
    driver.find_element(By.XPATH, '//input[@value="Log in"]').click()
    sleep(3)
    driver.save_screenshot('./image.png')
