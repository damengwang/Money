#-*- coding: utf8 -*-

# 思路：先随机出来m个数，然后平均分成m个数字只和的份数，然后将钱平均分给m个人#
import random
import smtplib

def checkparam(total,num):
    if(type(num) != type(1)):
        print "num must be Integer";
        return False;
    if(num < 0):
        print "num must be Positive Integer";
        return False;
    return True;

def roll(total,num,cond):
    #print "===红包算法研究程序==="
    #print "共",total,"元钱。分",num,"份。条件参数为：",cond
    total *= 100
    if(checkparam(total,num)):
        p = []
        average = total/num
##        print "前置平均数",average
        pre = []
        allpre = 0.0
        for count in range(0,num):
            tp = random.randint(1,10**cond)
            pre.append(tp)
            allpre += tp
##        print "预备随机序列",pre,len(pre)
##        print "预备总数",allpre
        onepre = round(total/allpre,cond)
##
##        print "预备单份额",onepre
##        print "预备总金额",onepre * allpre
        print '-------'
        alltp = 0
        for m in range(0,len(pre)-1):
            tp = int(onepre*pre[m])
            if (0==tp):
                tp = 1
            alltp += tp
            p.append(tp/100.0)
        last = total-alltp
        p.append(last/100.0)
        alltp += last
        #p.sort()
        #sorted(p)[0]
        #print "运气王:",sorted(p)[num-1]#,p[num-1]
        #random.shuffle(p)
        #print "红包序列",p,len(p)
        #print "总共发出",alltp/100.0

        #random.shuffle(p)      #打乱序列

        for i in range(0,len(p)):
            p[i]+=500.00
        print str(p)

#总金额，份数，调控参数（调控平均差）
roll(1000,8,10)
