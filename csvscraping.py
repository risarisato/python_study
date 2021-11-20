# ライブラリのインポート
import os
import random
from time import sleep
# 上記はもともとpythonにあるライブラリ

# 下記はPIPでインストしたライブラリ
import pandas as pd
import requests


# この状態で保存すると、画像ファイルでいっぱいになる
# 新しいフォルダ作成して、そこに保存する
# IMAGE_DIRは大文字は定数を表現する意味

# windowsなのでPATHを「r」をつけてあげると通りやすいr'C:\Users\

IMAGE_DIR = './images/'

# CSVファイルの読み込み
df = pd.read_csv('_____CSVファイル______')

# このIMAGE_DIRがありますか？
if os.path.isdir(IMAGE_DIR):
    print('すでにあります')
else:
    os.makedirs(IMAGE_DIR)


""" 
 '名前': name,
 '元のURL先': row_url,
 'Yahooからの検索イメージ': yahoo_image_url,
 'タイトル': title


# 画像の保存
df.name, df.yahoo_image_url

# 2以上を繰り返すはときは「zip」でまとめてあげる
zip(df.name, df.yahoo_image_url)

# zipの中を「in」してあげる
in zip(df.name, df.yahoo_image_url)

 """
# あとはfor文で回す
# write:書き込み、binary：バイナリー、ｆはfileで慣習でｆにする
# 全部取り出すと時間がかかるので先頭の5個だけ取り出す[:5]
# file_nameとyahoo_image_urlをデータフレームCSVのin zipの名前 Yahooからの検索から取り出す
# プログラミングで日本語表記はNGになる

for file_name, yahoo_image_url in zip(df.名前, df.Yahooからの検索イメージ):
    requests.get(yahoo_image_url)
    image = requests.get(yahoo_image_url)

    # 下記の2行で画像の保存
    with open(IMAGE_DIR + file_name + '.jpg', 'wb') as f:
        f.write(image.content)
    sleep(1)

    # import randomでsleep時間をランダムにして、人間っぽい動きを作る
    # sleepもforの中で使ってあげないといけない
    sleep(random.randint(1, 4))
