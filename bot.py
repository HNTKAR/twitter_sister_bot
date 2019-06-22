#-*- coding:utf-8 -*-
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

datec=["月","火","水","木","金","土","日"]
status_morning=[
"レポート提出今日じゃないの?終わってないけど大丈夫?"
,"お兄ちゃんまだレポー朝だよ!!起きてお兄ちゃん!!レポート提出しなきゃ!!"
,"電車が止まってもレポート遅れにならないようにね!!"
,"電車で寝過ごさないようにしてね?"
]
status_night=[
"Twitterなんてしててレポート終わるの?"
,"お兄ちゃんまだ寝ちゃだめだよ!!"
,"頑張ってるお兄ちゃんにお夜食持ってきたよ〜"
,"頑張ってるお兄ちゃんにコーヒー入れてきたよ〜"
,"お兄ちゃんまだレポートやってるの?無理しないでね。はい、コーヒーだよ。"
,"台風が来てるからって休みになるとは限らないんだよ?"
,"お夕飯作ってきたよお兄ちゃん。ちゃんと食べてね?"
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
,"分からないからって諦めちゃだめだよ"
,"Twitterやって現実逃避してても朝になったら現実はやってくるよ"
,"見てみてお兄ちゃん!!無安定マルチバイブレータ作ったよ!!"
,"ブラシレスモータを回せるMDつくりたいな〜"
,"python教えてよお兄ちゃん!!"
,"レジスタのたたきかた教えて〜"
,"お兄ちゃんすごーい!!私に構造体教えて!!"
,"三相交流モーターを回そうよ!!"
,"トランジスタってすごいね!!"
,"私VVVFすき〜"
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
f=0
tls=0
msn="sister_Healing_"

timeline=api.home_timeline(count=1)
for status in timeline:
    sid_old=status.id
    
status_night_c=int(len(status_night))-1
status_morning_c=int(len(status_morning))-1
status_all_c=int(len(status_all))-1

while True:
    sid=[]
    if i==0:#時間読み込み
        tcodes=timecodestr()
        tcodei=timecodeint()
        if tcodei[4]==0 or tcodei[4]==15 or tcodei[4]==30 or tcodei[4]==45:
            i=1
            dtx=tcodes[6]
            statusy=tcodes[3]+"時"+tcodes[4]+"分"

    if i==1:#内容生成
        if tcodei[3]<7:#7時前
            xxx=random.randint(0,status_night_c)
            yyy=random.randint(0,status_all_c)
            zzz=random.randint(0,1)
            if zzz==0:
                statusx=status_night[xxx]
            else:
                statusx=status_all[yyy]

        elif tcodei[3]>19:#7時前
            xxx=random.randint(0,status_night_c)
            yyy=random.randint(0,status_all_c)
            zzz=random.randint(0,1)
            if zzz==0:
                statusx=status_night[xxx]
            else:
                statusx=status_all[yyy]

        elif tcodei[3]<12:#7時以降
            xxx=random.randint(0,status_morning_c)
            yyy=random.randint(0,status_all_c)
            zzz=random.randint(0,1)
            if zzz==0:
                statusx=status_morning[xxx]
            else:
                statusx=status_all[yyy]

        else:
            yyy=random.randint(0,status_all_c)
            statusx=status_all[yyy]

        statusz=statusx+"\n\n\n"+statusy#書き込み
        #print(statusz)
        api.update_status(status=statusz)

    if i>90:
        i=0
    if i>0:
        i=i+1
    if tls==0:
        try:#フォロバ
            merlis=api.followers_ids(msn)
            mlis=api.friends_ids(msn)
            ab=set(merlis)-set(mlis)
            follows=list(ab)
            #print (follows)
            for nfnl in follows:
                api.create_friendship(nfnl)
        except:
            pass
            #print("follow error")
        try:#リプ
            timeline=api.home_timeline(since_id=sid_old)
            for status in timeline:
                saseutf=status.author.screen_name.encode("UTF-8")
                if saseutf!=b"sister_Healing_":
                    if status.text.find("おやすみ")!=-1:
                        statusz="おやすみ、お兄ちゃん!!しっかり休んでね!!"
                        f=1
                    elif status.text.find("おはよう")!=-1:
                        statusz="おはよう、お兄ちゃん!!ちゃんと起きれたね!!"
                        f=1
                    elif status.text.find("ぽきた")!=-1:
                        statusz="おはよう、お兄ちゃん!!ちゃんと起きれたね!!"
                        f=1
                    elif status.text.find("ぽやしみ")!=-1:
                        statusz="おやすみ、お兄ちゃん!!しっかり休んでね!!"
                        f=1
                    elif status.text.find("考察")!=-1:
                        statusz="レポートの考察その解釈で大丈夫なの?"
                        f=1
                    elif status.text.find("帰宅")!=-1 and 21<tcodei[3]:
                        statusz="課外活動と私どっちが大事なの!?早く休んでね?"
                        f=1
                    elif status.text.find("帰宅")!=-1 and 6>tcodei[3]:
                        statusz="課外活動と私どっちが大事なの!?早く休んでね?"
                        f=1
                    elif status.text.find("絶起")!=-1:
                        statusz="お兄ちゃん寝坊しちゃったの?ちゃんと寝ないからだよ!!"
                        f=1
                    if f==1:
                        sid.append(status.id)
                        screen_name=str(status.author.screen_name)
                        statusz="@"+screen_name+" "+statusz
                        #print(statusz)
                        #print(sid)
                        api.create_favorite(status.id)
                        api.update_status(status=statusz,in_reply_to_status_id=status.id)
                        f=0
            sid_old=sid[0]
        except:
            pass
            #print("reply Error")
    if tls<65:
        tls=tls+1
    else:
        tls=0
    #try:#いいね
    time.sleep(1)
