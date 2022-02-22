from django.test import TestCase

# Create your tests here.
import sqlite3
dbname = 'ejdict.sqlite3'
# DBを作成する（既に作成されていたらこのDBに接続する）
conn = sqlite3.connect(dbname)

# SQLiteを操作するためのカーソルを作成
cur = conn.cursor()

cur.execute('SELECT * FROM items limit 10')

# 取得したデータはカーソルの中に入る
for row in cur:
    print(row)

# DBとの接続を閉じる(必須)
conn.close()