#template
#from collections import deque

def getArgs():
    seq01=list(map(int,input().split()))
    seq02=list(map(int,input().split()))

    seqs=zip(seq01,seq02)
    return seqs

def judge(a,b):
    if(a>b):
        print('A')
    elif(a<b):
        print('B')
    else:
        print('D')

def tempfunction(seqs):
    wcnt_a,wcnt_b=0,0
    for a,b in seqs:
        if(a-b>0):
            wcnt_a+=1
        elif(a-b<0):
            wcnt_b+=1
        else:
            continue
    judge(wcnt_a,wcnt_b)

seqs=getArgs()
tempfunction(seqs)

