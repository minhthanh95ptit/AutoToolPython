from selenium import webdriver
import urllib
from PIL import Image
from twocaptcha import TwoCaptcha
import time
from fake_useragent import UserAgent
from threading import Thread
import random
import requests

solver = TwoCaptcha('f668b604d0954938b5c223f22ca1f90c')

def tool(thread):
    count = 0
 
    arrAdded = []

    for job in range(1,10):
        try:
            ua = UserAgent()
            userAgent = ua.random

            PROXY = randomIP(API_KEY_LIST[thread])
            print("CONNECT {}".format(PROXY))

            chrome_options = webdriver.ChromeOptions()

            chrome_options.add_argument(f'user-agent={userAgent}')
            chrome_options.add_argument('--proxy-server=%s' % PROXY)
            chrome_options.add_argument("--window-size=300,400")

            print(userAgent)
            
            PATH = '/home/ngocdoanh/Desktop/Cheat-ref-5/chromedriver_linux64/chromedriver'

            driver = webdriver.Chrome(PATH, chrome_options=chrome_options)

            driver.get("https://www.share288.com//xml/index.html#/register")

            print(driver.title)
            
            i = random.randint(1, 100000)

            sdt = 372000000 + i 

            if sdt in arrAdded:
                continue
            else:
                arrAdded.append(sdt)

            print(thread)
            imageURL = './captcha/{}.png'.format(thread)

            image = driver.find_elements_by_class_name("van-image__img")[0].screenshot(imageURL)

            token = solver.normal(imageURL)

            codeCaptcha = token['code']

            print(codeCaptcha)

            strSDT = "0{}".format(sdt)
    
            tel = strSDT
            code = codeCaptcha
            password = '123456'
            repassword = '123456'
            invite = '0823298'
        
            driver.find_element_by_xpath("//input[@type='tel'][@placeholder='Vui lòng nhập số điện thoại']").send_keys(tel)
            driver.find_element_by_xpath("//input[@type='tel'][@placeholder='Vui lòng nhập mã xác nhận']").send_keys(code)
            driver.find_element_by_xpath("//input[@type='password'][@placeholder='Xin hãy điền mật khẩu']").send_keys(password)
            driver.find_element_by_xpath("//input[@type='password'][@placeholder='Vui lòng xác nhận mật khẩu của bạn']").send_keys(repassword)
            driver.find_element_by_xpath("//input[@type='text'][@placeholder='Vui lòng nhập mã mời']").send_keys(invite)

            driver.find_element_by_xpath("//button[@class='van-button van-button--danger van-button--large van-button--block van-button--round']").click()

            time.sleep(1)

            current_url = driver.current_url

            if current_url == 'https://www.share288.com//xml/index.html#/register':
                time.sleep(80)
                driver.quit()
            else:
                count += 1
                print(count)
                print(strSDT)

                with open("sdt.txt","a") as f:
                    f.write("{}\n".format(strSDT))
                    f.close()
                    driver.quit()
                    time.sleep(80)
        except:
            time.sleep(80)
            driver.quit()
            continue
    return 0

def randomIP(API_KEY):

    url1 = "http://proxy.tinsoftsv.com/api/getProxy.php"
    url2 = "http://proxy.tinsoftsv.com/api/changeProxy.php"


    params1 = {
        'key': API_KEY,
    }

    params2 = {
        'key': API_KEY,
        'location': 0
    }


    while True:
        proxy = ''

        res = requests.get(url1, params=params1)
        
        print(res.text)

        if not res:
            time.sleep(10)
            continue
        
        if 'proxy' in res.json():
            if res.json()['next_change'] == 0:
                requests.get(url2, params=params2)
                continue
            else:
                proxy = res.json()['proxy']
                break
        else:
            time.sleep(15)
            requests.get(url2, params=params2)
            continue  
    
    return proxy
      
API_KEY_LIST = [
    'TLZoG6ZcW3puGJnFgLi3fFe4OwS2Nm3uj24Kmq',
    'TLQcU3xGCmQQ3iU9rTbMEdKjqhA5uFb9GJ6obW',
    'TLx5NVIWBWGQgwVKtIn6gmwtbiRIz0sAFW9H0O',
    'TLszdJpXQezx6ZkikRUwNavdhsKY5VrkJtcNt6',
    'TL4F6OgyYkh0TQ9q1ZFafNRZx9y8y5VeqrNLgd'
]

def main():
    for thread in range(5):
        t = Thread(target=tool, args=(thread,))
        t.start()

    print("DONE")

if __name__ == "__main__":
    main()

