#browser_amazon_app
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
# import chromedriver_binary
import time

def login():
    chrome = webdriver.Chrome("./driver/chromedriver.exe")

    chrome.get("https://www.amazon.co.jp/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.co.jp%2F%3Ftag%3Dhydraamazonav-22%26hvadid%3D39595899217%26hvpos%3D1t1%26hvexid%3D%26hvnetw%3Dg%26hvrand%3D4333793011701623001%26hvpone%3D%26hvptwo%3D%26hvqmt%3De%26hvdev%3Dc%26ref%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=jpflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

    #email = "e-mail"
    email = input("Amazonに登録しているメールアドレスを入力してください：")

    # ログイン情報のE-mailをinput入力された情報を基にセット
    emailTextBox = chrome.find_element_by_name("email")
    emailTextBox.send_keys(email)

    # 次へすすむボタンをクリック
    btmNext = chrome.find_element_by_id("continue")
    # print("btmNext:::pass")
    btmNext.click()
    time.sleep(3)
    
    #password = "password"
    password = input("ログイン時のパスワードを入力してください：")

    # ログイン情報のpasswordをinput入力された情報を基にセット
    passTextBox = chrome.find_element_by_id("ap_password")
    passTextBox.send_keys(password)

    # ログインボタンをクリック
    chrome.find_element_by_id("signInSubmit").click()

    time.sleep(3)

    chrome.find_element_by_id("nav-orders").click()
    time.sleep(3)

    return chrome

def download_receipt(chrome):
    # try:
    # print(page_items)
    yearCount = 0

    chrome.find_element_by_class_name("a-dropdown-prompt").click()
    chrome.find_element_by_id("orderFilter_" + str(yearCount+2)).click()

    page_items = chrome.find_elements_by_class_name('a-box-group')
    for j,k in enumerate(page_items):
        chrome.find_elements_by_class_name('a-box-group')[j].find_elements_by_class_name('a-popover-trigger')[-1].click()
        chrome.implicitly_wait(3)
        # chrome.find_element_by_class_name('a-popover').find_element_by_class_name('a-list').click()
        chrome.find_elements_by_class_name('a-popover')[0].find_elements_by_class_name('a-link-normal')[-1].click()
        # print_webPage(chrome)
        chrome.back()
    
    pageList = chrome.find_elements_by_class_name("a-row")

    if pageList is None:
        yearCount += 1
        download_receipt(chrome)
        
    elif len(chrome.find_elements_by_class_name("a-row")[j].find_elements_by_class_name("a-normal")) > 0:
        chrome.find_element_by_css_selector("a").click()
        download_receipt(chrome)

            
    # if chrome.find_elements_by_class_name('a-last').find_element_by_class_name('a-last').find_element_by_css_selecter('a') is None:
    #     download_receipt(chrome)
    # elif len(chrome.find_elements_by_class_name('a-last').find_element_by_class_name('a-last').find_element_by_css_selecter('a')) > 0:
    #     herf = chrome.find_elements_by_class_name('a-last').find_element_by_class_name('a-last').find_element_by_css_selecter('a').get_attribute("href")
    #     chrome.get(href)
    #     download_receipt(chrome)
        # chrome.back()
    # except:
        #     print("データ取得エラー")



    return chrome

def print_webPage(chrome):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "download.default_deirectory": "~/Downloads"
    })

    options.add_argument('--kiosk-printing')

    driver = webdriver.Chrome(options=options)
    driver.execute_script('window.print();')


if __name__ == "__main__":
    browser = login()
    browser = download_receipt(browser)
    browser.quit()

    
