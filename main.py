from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium 

PATH = 'geckodriver.exe'
url='https://twitter.com/overgap'
browser=webdriver.Firefox(executable_path=PATH)

browser.get(url)

search=browser.find_element(By.NAME,"s")
search.send_keys("Java")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "main")))
    articles=main.find_elements(By.TAG_NAME,'article')
    for a in articles:
        time=a.find_element(By.TAG_NAME,'time')
        print(time.text, end="\n\n")
    print(type(articles))
finally:
    browser.quit()

