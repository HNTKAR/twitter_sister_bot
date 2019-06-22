import tweepy
import datetime
import time
import random

# 各種キーをセット
CONSUMER_KEY = "key"
CONSUMER_SECRET = "key"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN = "key"
ACCESS_SECRET = "key"
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
i=0

datec=["月","火","水","木","金","土","日"]
status_morning=[
"レポート提出今日じゃないの?終わってないけど大丈夫?"
,"お兄ちゃんまだレポー朝だよ!!起きてお兄ちゃん!!レポート提出しなきゃ!!"
,"電車が止まってもレポート遅れにならないようにね!!"
]
status_night=[
"Twitterなんてしててレポート終わるの?"
,"お兄ちゃんまだ寝ちゃだめだよ!!"
,"頑張ってるお兄ちゃんにお夜食持ってきたよ〜"
,"お兄ちゃんまだレポートやってるの?無理しないでね。はい、コーヒーだよ。"
]
status_all=[
"もう!!また栄養剤なんて飲んで!!体に悪いよ?"
,"お兄ちゃん私の写真見て何笑ってるの?"
,"レポートの進捗はどう?"
,"うわ〜すごーい!!難しいこと書いてるね!!"
,"この考察間違えてない?"
,"表題とか忘れてない?"
,"表紙の確認はした?"
,"回路図間違えてない?"
,"ちゃんと引用したら引用元を書いておこうね?"
]
status17="" #投稿するツイート
status18="" #投稿するツイート
status19="" #投稿するツイート

def timecodestr():
    now = datetime.datetime.now() # 現在の日時を取得
    dtx=now.weekday()
    sny=str(now.year)
    snm=str(now.month)
    snd=str(now.day)
    snh=str(now.hour)
    snn=str(now.minute)
    sns=str(now.second)
    return sny,snm,snd,snh,snn,sns,dtx


def timecodeint():
    now = datetime.datetime.now() # 現在の日時を取得
    sny=int(now.year)
    snm=int(now.month)
    snd=int(now.day)
    snh=int(now.hour)
    snn=int(now.minute)
    sns=int(now.second)
    return sny,snm,snd,snh,snn,sns

i=0
a=[0,0]
status_old_id=1013455124549627904
while True:
    try:
        timeline=api.mentions_timeline(count=5)
        for status in timeline:
            status_id=status.id
            if status_id>status_old_id:
                a.append(status_id)
                print(status_id)
                screen_name=status.author.screen_name.encode("UTF-8")
                reply_text="@"+screen_name+" "+"はじめまして、お兄ちゃん!!"
                api.update_status(status=reply_text,in_reply_to_status_id=status_id)
        a.sort()
        status_old_id=a[0]
    except:
        pass
    if i==0:
        tcodes=timecodestr()
        tcodei=timecodeint()
        if tcodei[4]==0:
            i=1
        elif tcodei[4]==15:
            i=1
        elif tcodei[4]==30:
            i=1
        elif tcodei[4]==45:
            i=1
        else:
            i=0
        dtx=tcodes[6]
        statusy=tcodes[0]+"年"+tcodes[1]+"月"+tcodes[2]+"日"+"("+datec[dtx]+")"+"\n"+tcodes[3]+"時"+tcodes[4]+"分"

    if i==1:
        if tcodei[3]<7:#7時前
            xxx=random.randint(0,3)
            yyy=random.randint(0,8)
            zzz=random.randint(0,1)
            if zzz==0:
                statusx=status_night[xxx]
            else:
                statusx=status_all[yyy]

        elif tcodei[3]>19:#7時前
            xxx=random.randint(0,3)
            yyy=random.randint(0,8)
            zzz=random.randint(0,1)
            if zzz==0:
                statusx=status_night[xxx]
            else:
                statusx=status_all[yyy]

        elif tcodei[3]<12:#7時以降
            xxx=random.randint(0,2)
            yyy=random.randint(0,8)
            zzz=random.randint(0,1)
            if zzz==0:
                statusx=status_morning[xxx]
            else:
                statusx=status_all[yyy]

        else:
            yyy=random.randint(0,8)
            statusx=status_all[yyy]



    if i==1:
        statusz=statusx+"\n\n\n"+statusy
        #print(statusz)
        api.update_status(status=statusz)
        
        try:
            for follower in tweepy.Cursor(api.followers).items():
                follower.follow()
        except:
            pass
        try:
            timeline=api.mentions_timeline()
            for status in timeline:
                print (status.text)
        except:
            print("TL error")
    if i>65:
        i=0
    if i>0:
        i=i+1
    time.sleep(1)
