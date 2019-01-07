from twython import Twython
import Token
import json
import urllib.request
from requests_oauthlib import OAuth1Session
import datetime
import re

#APIキー
twitter = Twython(Token.CONSUMER_KEY,Token.CONSUMER_SECRET,Token.ACCESS_KEY,Token.ACCESS_SECRET)
#通知がほしいアカウント名
username = Token.username
#遅延情報のrss
url = 'https://rti-giken.jp/fhc/api/train_tetsudo/delay.json'
#jsonファイルを開く
D_json = urllib.request.urlopen(url)
#dataにjsonファイル読み込む
data=D_json.read().decode('utf-8')
#遅延情報を知りたい路線の名前をリスト化
sen = ['京浜東北', '中央・総武各駅停車','総武本', '山手']
#結果変数の宣言
result = ''
 #現在時間を取得
dt_now=datetime.datetime.now()
#stringに変換
h=dt_now.strftime("%Y/%m/%d %H:%M:%S")
#遅延の判定
for delay in sen:
    if  delay in data:
        result += delay + '線'
#BOTのuserID
user = Token.userID
#何件のツイートを読み込むか
count =10
#タイムラインの取得
timeline = twitter.get_user_timeline(user_id = user,count = count,since_id=10,exclude_replies = False)
#判定用変数
check = False
#タイムラインのループ
for tweet in timeline:
    #ツイートのテキストを取得
    tweettext = (tweet['text'])
    #ツイートの文字削除
    deltext = tweettext.strip('が遅延しています。')
    #リプライツイートを判定
    if tweet['in_reply_to_screen_name'] == username:
        #ツイートのテキストを取得
        tweettext = (tweet['text'])
       #テキストをカットする
        cuttweet = tweettext.splitlines()
        #2行目をdatetime型に変換
        tweetdate = datetime.datetime.strptime(cuttweet[1],'%Y/%m/%d %H:%M:%S')
       #現在の時間から15分引いた時間を代入
        date_check = dt_now - datetime.timedelta(minutes=15)
        #ツイート時間が15分前か判定、textが被っていないか判定
        if date_check < tweetdate and deltext == result:
           check = True
           break

#resultが空白、checkがTrueじゃないときにツイート
if result !='' and check != True :
   twitter.update_status(status='@' + username + result + 'が遅延しています' + '\n' + h)