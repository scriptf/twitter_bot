# -*- coding: utf-8 -*- 
import sys
import twitter

auth = twitter.OAuth(consumer_key="",
consumer_secret="",
token="",
token_secret="")

t = twitter.Twitter(auth=auth)

# pos.txt には tweets.txt の何行目を取得するか記録している
f1 = open('pos.txt')
pos = f1.readline().rstrip()
f1.close()

f2 = open('tweets.txt')
line = f2.readline().rstrip()
i = 1

# pos で指定した行を読みこむ
max = len(open('tweets.txt').readlines())
while line:
    if i == int(pos) :
        status = line 
        t.statuses.update(status=status)
        f3 = open('pos.txt','w')
        if i == max:
	    f3.write('1')
	    f3.close()
        else:
	    f3.write(str(i+1))
            f3.close()
    line = f2.readline().rstrip()
    i = i + 1

