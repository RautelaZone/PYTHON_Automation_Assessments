import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
BASE_URL = "https://www.makemytrip.com/"

driver.maximize_window()
driver.get(BASE_URL)

try:
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='commonModal__close']"))
    )
    close_button.click()
except Exception as e:
    print(f"Error closing modal: {e}")

try:
    view_all_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='View All']"))
    )
    view_all_link.click()
except Exception as e:
    print(f"Error clicking 'View All': {e}")
time.sleep(5)

window_handles = driver.window_handles
driver.switch_to.window(window_handles[-1])

actual_title = "MakeMyTrip - #1 Travel Website 50% OFF on Hotels, Flights & Holiday"
child_tab_title = driver.title

assert actual_title in child_tab_title

trending_radio_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Trending')]"))
    )
trending_radio_option.click()

driver.find_element(By.XPATH, "//p[text()='Plan your summer trips with Package Price Drop Days.']").click()

window_handles = driver.window_handles
driver.switch_to.window(window_handles[-1])

actual_title_1 = "MakeMyTrip"
child_tab_title_1 = driver.title

assert actual_title_1 in child_tab_title_1

book_now_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h2[text()='Get FLAT 30% OFF* on Holiday Packages.']/following::a[1]"))
    )
book_now_button.click()

driver.quit()

