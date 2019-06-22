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
            elif status.text.find("絶起")!=-1:
                statusz="お兄ちゃん寝坊しちゃったの?ちゃんと寝ないからだよ!!"
                f=1
            if f==1:
            sid.append(status.id)
            screen_name=str(status.author.screen_name)
            statusz="@"+screen_name+" "+statusz
            print(statusz)
            print(sid)
            api.update_status(status=statusz,in_reply_to_status_id=status.id)
            f=0
    sid_old=sid[0]