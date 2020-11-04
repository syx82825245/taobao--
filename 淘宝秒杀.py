from selenium import webdriver
import datetime
import time
def main():
    # 打开淘宝登录页，并进行扫码登录
    #https://detail.tmall.com/item.htm?id=605884215543&spm=a1z0k.6846577.0.0.6aa35e765uE1E4&_u=t2dmg8j26111
    browser = webdriver.Chrome()
    browser.get(url = 'https://www.taobao.com/')
    time.sleep(3)
    if browser.find_element_by_link_text("亲，请登录"):
        browser.find_element_by_link_text("亲，请登录").click()
        print("请在15秒内完成扫码")
        time.sleep(15)
        browser.get(-"https://detail.tmall.com/item.htm?id=605884215543&spm=a1z0k.6846577.0.0.6aa35e765uE1E4&_u=t2dmg8j26111")
        while True:
            now = datetime.datetime.now()
            #print(now.hour, now.minute, now.second)
            if now.hour == 10 and now.minute == 0 and now.second == 0:
                #print('开始抢购')

                browser.find_elements_by_id("J_LinkBuy")[0].click()
                browser.find_elements_by_class_name("go-btn")[0].click()

            time.sleep(0.01)

        time.sleep(30)
    else:
        print('登录失败')
    time.sleep(3)
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


main()
