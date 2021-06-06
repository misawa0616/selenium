from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

with webdriver.Chrome() as driver:
    driver.get("http://localhost:3000/checkbox-test")
    original_window = driver.current_window_handle
    wait = WebDriverWait(driver, 10)
    elements = driver.find_elements(By.TAG_NAME, "input")
    open_pdf_element = driver.find_element(By.LINK_TEXT, "PDF出力")
    driver.save_screenshot('./{}-{}-image.png'.format(0, 1))
    skip_count = 0
    for i in range(len(elements)):
        if i > 0:
            elements[i - 1].click()
        if skip_count > 0:
            skip_count -= 1
            continue
        if elements[i].get_attribute("type") == 'text':
            elements[i].send_keys("admin")
            elements[i + 1].click()
            driver.save_screenshot('./{}-{}-image.png'.format(i + 1, 1))
            open_pdf_element.click()
            wait.until(EC.number_of_windows_to_be(2))
            for window_handle in driver.window_handles:
                if window_handle != original_window:
                    driver.switch_to.window(window_handle)
                    break
            sleep(2)
            driver.save_screenshot('./{}-{}-image.png'.format(i + 1, 2))
            driver.close()
            driver.switch_to.window(original_window)
            elements[i].clear()
            skip_count += 1
        else:
            elements[i].click()
            driver.save_screenshot('./{}-{}-image.png'.format(i + 1, 1))
            open_pdf_element.click()
            wait.until(EC.number_of_windows_to_be(2))
            for window_handle in driver.window_handles:
                if window_handle != original_window:
                    driver.switch_to.window(window_handle)
                    break
            sleep(2)
            driver.save_screenshot('./{}-{}-image.png'.format(i + 1, 2))
            driver.close()
            driver.switch_to.window(original_window)
