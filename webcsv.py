from time import sleep

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_path = r'C:\Users\＿＿＿\Desktop\ScrapingBeginner-main\chromedriver.exe'

# --> STEP1 : Yahoo画像検索に自動でアクセスする(シークレットモード)
options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path = chrome_path, options = options)

url = 'https://______________'
driver.get(url)

sleep(3)

# --> STEP2 : プログラミングで検索する
query = '検索ワード'
search_box = driver.find_element_by_class_name('SearchBox__searchInput')
search_box.send_keys(query)
search_box.submit()

sleep(3)

height = 1000
while height < 5000:
    driver.execute_script("window.scrollTo(0, {});".format(height))
    height += 100
    print(height)

    sleep(1)

"""
beautifulsoupで言い換えるところのfind_allと同じ意味



find_elements_by_class_name()
find_element_by_class_name()

# 画像の要素を選択する
driver.find_elements_by_class_name('sw-Thumbnail sw-Thumbnail--tile')
→Seleniumの仕様により、name('sw-Thumbnail sw-Thumbnail--tile')は出来ない

"""

# 画像の要素(elements)を選択する
elements = driver.find_elements_by_class_name('sw-Thumbnail')

"""
# 要素からURLを取得する
# 番号を振り分けるの→emunerate
for element in elemnts:

"""

# yahoo検索の要素からのURLを取得する
# 番号を振り分けるの→emunerate
# 番号をiとしてstartを1からはじめる
# find_element_by_tag_name()は「h2、b、img」とか
# find_element_by_tag_name()は「h2、b、img」がattributeの「scr」のなかにある

"""
for element in emunerate(elemnts, start=1):
    yahoo_image_url element.find_element_by_tag_name('img').get_attribute('scr')

# 元々のHPデータの画像のURL
    row_url = elment.find_element_by_class_namae('sw-ThumbnailGrid__details').get_atttibute('href')

# 画像のタイトル→URLだけあってもわかりにくいため
    title = elment.find_element_by_class_namae('img').get_atttibute('alt')

# 画像保存すると名前があるとわかりやすい
# query検索文字に「i番号」を「f」でループさせる
    name = f'{query}_{i}'

"""
# 辞書に格納
d_list =[]

# プログラム順次実行させるため順番変更
for i, element in enumerate(elements, start=1):
    name = f'{query}_{i}'
    row_url = element.find_element_by_class_name('sw-ThumbnailGrid__details').get_attribute('href')
    yahoo_image_url = element.find_element_by_tag_name('img').get_attribute('src')
    title = element.find_element_by_tag_name('img').get_attribute('alt')

    d = {
        '名前': name,
        '元のURL先': row_url,
        'Yahooからの検索イメージ': yahoo_image_url,
        'タイトル': title
    }

    d_list.append(d)

    sleep(1)

df = pd.DataFrame(d_list)
df.to_csv('image_urls_20210514.csv', index=None, encoding='utf-8-sig')

driver.quit()
