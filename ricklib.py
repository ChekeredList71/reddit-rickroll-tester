from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import re

# load rickroll links
ricklinks = [i.strip() for i in open("ricklinks.txt")]


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
    waiter = WebDriverWait(driver, 6)
    waiter.until(EC.visibility_of_element_located((By.XPATH, "/html/body/shreddit-app/dsa-transparency-modal-provider/div/div[1]/div/main/shreddit-comment-tree/shreddit-comment/div[3]/div/p")))

    text = driver.find_element(By.XPATH, "/html/body/shreddit-app/dsa-transparency-modal-provider/div/div[1]/div/main/shreddit-comment-tree/shreddit-comment/div[3]/div/p").text
    driver.quit()
    return text


def is_link_valid(url: str):
    return re.match(r"https://www.reddit.com/[0-z]+/[0-z]+/comments/[0-z]+/comment/[0-z]+/\?", url) is not None


def is_text_ricked(text: str):
    for i in re.findall(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", str):
        if i in ricklinks:
            return True
    return False
