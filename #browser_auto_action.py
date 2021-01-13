#browser_auto_action.py

#seleniumの使いたいライブラリをインポート
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome("./driver/chromedriver.exe")

location = input("場所入力：")
favorite_foods = ["ラーメン","とんかつ","たこ焼き","しゃぶしゃぶ"]

for i, food in enumerate(favorite_foods):
    if i > 0:
        #新しいタブ
        chrome.execute_script("window.open('','_brank')")
        chrome.switch_to.window(chrome,window_handles[i])

    #グーグルを開く
    chrome.get("https://www.google.co.jp")

    #検索キーワードを入力
    search_box = chrome.find_element_by_name("q")
    search_words = location, food
    search_box.send_keys(" ".join(search_words))

    #検索実行
    search_box.send_keys(Keys.RETURN)
    print(chrome.titel)

#先頭のタブに戻る
chrome.switch_to.window(chrome.window_handles[0]) 
