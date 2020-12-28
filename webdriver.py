from selenium import webdriver
import urllib
from PIL import Image
from twocaptcha import TwoCaptcha
import time
from fake_useragent import UserAgent
from threading import Thread
import random

solver = TwoCaptcha('f668b604d0954938b5c223f22ca1f90c')

def tool():
    count = 0
    while True:
        try:
            ua = UserAgent()
            userAgent = ua.random

            chrome_options = webdriver.ChromeOptions()

            chrome_options.add_argument(f'user-agent={userAgent}')
            chrome_options.add_argument('--proxy-server=%s' % PROXY)
            chrome_options.add_argument("--window-size=300,400")

            print(userAgent)
            
            PATH = '/home/ngocdoanh/Desktop/Cheat-ref-5/chromedriver_linux64/chromedriver'

            driver = webdriver.Chrome(PATH, chrome_options=chrome_options)

            res = driver.get("https://www.share288.com//xml/index.html#/register")

            time.sleep(10)

            i = random.randint(1, 100000)

            imageURL = './captcha/{}.png'.format(i)
            image = driver.find_elements_by_class_name("van-image__img")[0].screenshot(imageURL)


            token = solver.normal(imageURL)

            codeCaptcha = token['code']

            print(codeCaptcha)

            sdt = 372482267 + i 

            strSDT = "0{}".format(sdt)
    
            tel = strSDT
            code = codeCaptcha
            password = '123456'
            repassword = '123456'
            invite = '0806917'
        
            driver.find_element_by_xpath("//input[@type='tel'][@placeholder='Vui lòng nhập số điện thoại']").send_keys(tel)
            driver.find_element_by_xpath("//input[@type='tel'][@placeholder='Vui lòng nhập mã xác nhận']").send_keys(code)
            driver.find_element_by_xpath("//input[@type='password'][@placeholder='Xin hãy điền mật khẩu']").send_keys(password)
            driver.find_element_by_xpath("//input[@type='password'][@placeholder='Vui lòng xác nhận mật khẩu của bạn']").send_keys(repassword)
            driver.find_element_by_xpath("//input[@type='text'][@placeholder='Vui lòng nhập mã mời']").send_keys(invite)

            driver.find_element_by_xpath("//button[@class='van-button van-button--danger van-button--large van-button--block van-button--round']").click()

            button = driver.find_element_by_xpath("//button[@class='van-button van-button--danger van-button--large van-button--block van-button--round']")

            time.sleep(20)

            if button.is_displayed():
                print("ERROR")
                time.sleep(20)
                continue
            else:
                count += 1
                print(count)

                with open("sdt.txt","a") as f:
                    f.write("{}\n".format(strSDT))
                    f.close()

            driver.quit()
        except:
            time.sleep(100)
            continue
    return 0

PROXY = '171.229.66.120:25889'

for i in range(5):
    t = Thread(target=tool)
    t.start()

print("DONE")

