import random
import time
from datetime import datetime, timedelta, timezone

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# 例外処理用のlibraryをimport
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
from pathlib import Path
import re
import platform
import json
import csv

# デバッグ中はTrueにする
is_debug = False
# is_debug = True

# 取得した詳細データを配列として入れる変数
list_output = []

print('start')

# タイムゾーンの生成
JST = timezone(timedelta(hours=+9), 'JST')

now = datetime.now(JST)
formatDateTime = now.strftime('%Y-%m-%d_%H:%M:%S')
print(formatDateTime)

# スクリプト開始時間
start = time.time()

driver = webdriver.Chrome(ChromeDriverManager().install())
time.sleep(random.randint(1, 2) / 10)


def download_stock_csv(code_range, save_dir):
    for code in code_range:
        # TODO: 都道府県をenumにして、番号で変更できるようにしたい。
        url = 'https://weathernews.jp/s/ski/area/gunma.html'.format(code)
        driver.get(url)

        # ページ内の何個目のリンクか
        product_index_in_page = 0
        detail_link_index = 1

        # ページ内の合計数
        area_sum = driver.find_element_by_xpath(
                    "/html/body/div[1]/div[3]/article/section[1]/h1/span").text

        # while product_index_in_page < int(area_sum):
        while product_index_in_page < 3:
            try:
                # 詳細ページを別タブで開く
                detail_link = driver.find_element_by_xpath("/html/body/div[1]/div[3]/article/section[1]/div/ul/li[%s]/a" % (detail_link_index))

                # 詳細クリック
                handles_before = driver.window_handles
                actions = ActionChains(driver) #(リンク)要素を新しいタブで開く
                if platform.system() == 'Darwin':
                    #Macなのでコマンドキー
                    actions.key_down(Keys.COMMAND)
                else:
                    #Mac以外なのでコントロールキー
                    actions.key_down(Keys.CONTROL)

                actions.click(detail_link)
                actions.perform()
                # driver.execute_script('arguments[0].click();', detail_link)
                WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located)
                time.sleep(random.randint(1, 2) / 10)
                # driver.switch_to.window(driver.window_handles[1])  # switch new tab
                time.sleep(1)

                #クリック後のハンドルリスト
                handles_after = driver.window_handles

                #ハンドルリストの差分
                handle_new = list(set(handles_after) - set(handles_before))

                #新しいタブに移動
                driver.switch_to.window(handle_new[0])


                # スキー場名
                area_name = driver.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/article[1]/section/div[1]/h1").text
                print("area_name: " + area_name)

                # 積雪量
                snow_volume = driver.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/article[1]/section/div[1]/div/div[1]/div[2]/div/div/p/span").text
                print("snow_volume: " + snow_volume)

                # コース数
                course = driver.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/article[1]/section/div[6]/div[3]/div/dl[1]/div[2]/dd").text
                print("course: " + course)

                # 住所
                address = driver.find_element_by_id("addr").text
                print("address: " + address)

                # リフト料金
                lift_charges = driver.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/article[1]/section/div[6]/div[3]/div/dl[1]/div[8]/dd").text
                print("lift_charges: " + lift_charges)

                # 営業時間
                business_hours = driver.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/article[1]/section/div[6]/div[3]/div/dl[2]/div[8]/dd").text
                print("business_hours: " + business_hours)

                original_page_url = url
                page_id = code

                site_name = 'weather_news'

                list_output.append(
                    [site_name, page_id, area_name, snow_volume, course, address, lift_charges, business_hours, original_page_url])

                # 詳細ページを閉じる
                print("詳細ページを閉じる")
                product_index_in_page += 1
                print(str(product_index_in_page) + "コ目完了")
                detail_link_index += 1
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

            except NoSuchElementException as e:
                print(e)
            time.sleep(1)


import os

download_stock_csv(range(1, 2), os.getcwd())

# ブラウザーを終了
driver.quit()

path_root = Path('').resolve()
path_output = path_root / 'output'
os.makedirs(path_output, exist_ok=True)

colums = ["site_name", "page_id", "area_name", "snow_volume", "course", "address", "lift_charges", "business_hours", "original_page_url"]
# CSVとして保存
# TODO: json形式で取得したい
# OUTPUT
FILENAME = 'ski_slope_map'
pd.DataFrame(list_output, columns=colums).to_csv(path_output / f'{FILENAME}.csv', index=False)

json_list = []

# CSVファイル読み込み
with open(f'{path_output}/{FILENAME}.csv', 'r') as f:
    for row in csv.DictReader(f):
        json_list.append(row)

print("A")

# JSONファイルへの書き込み
with open(f'{path_output}/{FILENAME}.json', 'w') as f:
    json.dump(json_list, f, ensure_ascii=False)

exit()
