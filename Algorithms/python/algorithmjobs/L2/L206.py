#template
from collections import deque
seqs=deque()

def getArgs():
    n=int(input())
    for i in range(n):
        seqs.append(list(map(int,input().split())))
    
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
print(seqs)
#tempfunction(seqs)

