from django.shortcuts import render

# Create your views here.
# 以下を追記
# def index(req):
#     return render(req, 'index.html')

# sqlite3からの取得処理
import sqlite3
dbname = 'ejdict.sqlite3'
# DBを作成する（既に作成されていたらこのDBに接続する）
conn = sqlite3.connect(dbname)

# SQLiteを操作するためのカーソルを作成
cur = conn.cursor()

symbol = 'apple'
cur.execute("SELECT * FROM items WHERE word = '%s'" % symbol)
# 取得したデータはカーソルの中に入る
for row in cur:
    # print(row)
    params = { # <- 渡したい変数を辞書型オブジェクトに格納
        'title': 'Hi Django!',
        'subtitle': row,
    }

# # DBとの接続を閉じる(必須)
conn.close()

# index.htmlへリクエスト
def index(req):
    dbname = 'ejdict.sqlite3'
    # DBを作成する（既に作成されていたらこのDBに接続する）
    conn = sqlite3.connect(dbname)

    # SQLiteを操作するためのカーソルを作成
    cur = conn.cursor()
 
    symbol = req.POST['nyuryoku1']
    cur.execute("SELECT * FROM items WHERE word = '%s'" % symbol)

    for row in cur:
        # print(row)

        # params = { # <- 渡したい変数を辞書型オブジェクトに格納
        #     'title': 'Hi Django!',
        #     'subtitle': row,
        #     'nyuryoku1': req.POST['nyuryoku1'],
        # }
        params = { # <- 渡したい変数を辞書型オブジェクトに格納
            'title': 'Hi Django!',
            'subtitle': row,
            'nyuryoku1': req.POST['nyuryoku1'],
        }

    # DBとの接続を閉じる(必須)
    conn.close()

    # return render(request, 'hello/index.html', params) # <- 引数にparamsを追記
    return render(req, 'index.html', params) # <- 引数にparamsを追記
