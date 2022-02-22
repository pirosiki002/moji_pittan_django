from django.shortcuts import render

# Create your views here.
# 以下を追記
# def index(req):
#     return render(req, 'index.html')

# sqlite3からの取得処理
import sqlite3

# index.htmlへリクエスト
def index(req):

    dbname = 'ejdict.sqlite3'
    # DBを作成する（既に作成されていたらこのDBに接続する）
    conn = sqlite3.connect(dbname)

    # SQLiteを操作するためのカーソルを作成
    cur = conn.cursor()

    # symbol = req.POST['nyuryoku1']
    symbol = req.POST.get('nyuryoku1')
    cur.execute("SELECT * FROM items WHERE word = '%s'" % symbol)

    explain = ''
    #こんな回りくどいことしなくてもよさそう
    for row in cur:
        explain = row

    params = { # <- 渡したい変数を辞書型オブジェクトに格納
        'title': 'Hi Django!',
        'subtitle': explain,
        'nyuryoku1': symbol,
        # 'subtitle': row,
    }

    # DBとの接続を閉じる(必須)
    conn.close()

    return render(req, 'index.html', params) # <- 引数にparamsを追記
    # return render(req, 'index.html') # <- 引数にparamsを追記
