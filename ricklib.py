from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import re


def extract_comment(url: str):
    # set up headless mode (so the Google Chrome window doesn't open)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    # fake the user-agent
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

    # init webdriver component and launch page
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # when in headless mode, driver.find_element will fail, because the website doesn't load the comment when immediately
    # we need to wait for the browser to take the JavaScript AJAX request, and then scrape it
    waiter = WebDriverWait(driver, 3)
    waiter.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#t1_kscnr2t-comment-rtjson-content")))

    text = driver.find_element(By.CSS_SELECTOR, "#t1_kscnr2t-comment-rtjson-content > div:nth-child(1) > p:nth-child(1)").text
    driver.quit()
    return text


def is_link_valid(url: str):
    return re.match(r"https://www.reddit.com/r/[0-z]+/comments/[0-z]+/comment/[0-z]+/\?", url) is not None

