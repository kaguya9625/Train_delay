#このプログラムはraspberry piで稼動しているTwitterBotで電車の遅延情報をリプライしてくれるソースコードです。  
完全に自分用の物なので、路線名などは自分が使う物、また近いものを使用しています。  

使用する場合別ファイルに(このソースではToken.py)  

TwitterAPIキー  
CONSUMER_KEY = ''   
CONSUMER_SECRET = ''   
ACCESS_KEY = ''  
ACCESS_SECRET = ''  

BOTの数字のuserIDを記載してください  
userID =  

通知がほしいアカウントの＠を抜いたID  
username = ''  


#遅延情報はこちらのjsonから取得しています。 "https://rti-giken.jp/fhc/api/train_tetsudo/"  