from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

#op=Options()
#op.add_experimental_option("detach",True)

options=Options()
options.add_experimental_option('excludeSwitches',['enable-logging'])
options.add_experimental_option("detach",True)


PATH="chromedriver.exe"
url=["https://orteil.dashnet.org/cookieclicker/","https://www.techwithtim.net/"]
driver=webdriver.Chrome(PATH,chrome_options=options)
#driver=webdriver.Chrome(PATH)
driver.implicitly_wait(10)
driver.get(url[0])

driver.find_element(By.XPATH,"/html/body/div[1]/div/a[1]").click()
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/button[1]/p").click()
driver.find_element(By.XPATH,'//*[@id="langSelect-EN"]').click()

cookies=driver.find_element(By.ID, "bigCookie")
cookies_counter=driver.find_element(By.ID, "cookies")

items=[driver.find_element(By.ID, "productPrice"+str(i)) for i in range(1,-1,-1)]

actions=ActionChains(driver)

for i in range(5000):
    actions.click(cookies)
    actions.perform()
    counter=int(cookies_counter.text.split(" ")[0])
    for item in items:
        price=int(item.text)
        if(counter>=price):
            upgrade_item=ActionChains(driver)
            upgrade_item.double_click(item).double_click(item)
            upgrade_item.perform()

