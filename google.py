from hashlib import new
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from slacker import Slacker
import time
import requests

driver = webdriver.Chrome()
driver.get("http://www.google.com")

elem = driver.find_element_by_name("q") 
elem.send_keys("클라우드엔지니어 채용") 
elem.send_keys(Keys.RETURN) 

driver.find_element_by_class_name("esVihe").click()

itemlist = driver.find_element_by_class_name("zxU94d")

SCROLL_PAUSE_TIME = 1

cnt = 0
while True:
    driver.execute_script("arguments[0].scrollBy(0, 1000)", itemlist)
    
    time.sleep(SCROLL_PAUSE_TIME)

    cnt += 1

    if cnt >= 10:
        break
    else:
        continue   

urls = driver.find_elements_by_class_name("pMhGee")

urlList = []

for url in urls:
    urlList.append(url.get_attribute("href"))

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-1844744389825-1817470521015-m0e1eejgV2FvWyIZ0xJeIEUP"

count = 0

for i in range(len(urlList)):
    post_message(myToken,"#project", urlList[i])
    count = count + 1

print(count)

driver.close()

# https://github.com/JAEHYUN2022/recruiteSite.git