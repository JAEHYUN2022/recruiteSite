# 🍎 Web Crawling
<br/><br/>

## 기능
<<<<<<< HEAD
- 웹 크롤링을 통한 "클라우드엔지니어 채용"에 관련한 웹사이트들을 추출한다.
- 추출된 웹사이트를 Slack를 활용하여 모바일로 확인할 수 있도록 한다. <br/><br/><br/>

## 사용 기술
- Selenium <br/>
- Python <br/><br/><br/>

## 코드 설명
1. 크롬 브라우저를 통해 구글 웹 사이트에 접속한다.
```python
driver = webdriver.Chrome()
driver.get("http://www.google.com")
```
<br/><br/>

2. 검색창을 찾아서 "클라우드엔지니어 채용"을 입력한 후 ENTER키를 누른다.
```python
elem = driver.find_element_by_name("q") 
elem.send_keys("클라우드엔지니어 채용") 
elem.send_keys(Keys.RETURN) 
```
<img src="./Image/1.png"> <br/><br/>
<br/><br/>

3. 현재는 3개의 채용 정보밖에 보이지 않으므로 아래 채용 정보 더보기를 클릭한다.
```python
driver.find_element_by_class_name("esVihe").click()
```
<img src="./Image/2.png"> <br/><br/>
<br/><br/>

4. 왼쪽 공고 박스부분의 스크롤을 계속해서 내리며 모든 채용공고를 확인할 수 있도록 한다.
```python
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
```
<img src="./Image/3.png"> <br/><br/>

5. 개발자도구를 통해 모든 채용공고의 href 주소를 핸드폰과 연동된 Slack 메신저에 출력한다.
```python
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

for i in range(len(urlList)):
    post_message(myToken,"#project", urlList[i])

driver.close()
```
<img src="./Image/4.png"> <br/>
<img src="./Image/5.png"> 
=======
1. 웹 크롤링을 통한 "클라우드엔지니어 채용"에 관련한 웹사이트들을 추출한다.
2. 추출된 웹사이트를 Slack를 활용하여 모바일로 확인할 수 있도록 한다.



>>>>>>> 6f79f6083cbed841950c8be5a7f8cb17eb915b9a
