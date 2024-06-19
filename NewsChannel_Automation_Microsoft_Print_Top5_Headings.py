from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
BASE_URL = "https://www.ndtv.com/"
news_topic_text = "Tech"
how_many_topics = 5

driver.maximize_window()
driver.get(BASE_URL)

try:
    news_topic = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='" + news_topic_text + "']"))
    )
    news_topic.click()
    print(f"Clicked on {news_topic_text}")
except Exception as e:
    print(f"Error clicking news topic: {e}")

try:
    headings = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//h3[@class='trenz_news_head lh22 listing_story_title']"))
    )
    print("Top Headings are:")
    for i in range(min(len(headings), how_many_topics)):
        print(headings[i].text)

except Exception as e:
    print(f"Error retrieving headings: {e}")

driver.quit()
