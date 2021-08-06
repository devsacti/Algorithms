import sys
input=sys.stdin.readline

def dpMarble(n):
    if(n>3):dptable=['*']*(1+n) # for 1 based indexing
    else:dptable=['*']*(1+3)

    dptable[1]=1
    dptable[2]=1
    dptable[3]=1

    for i in range(5,n+1):
        #sub problems
        tokens=[]
        # 철수가 주어진 n개에 대해 1개,2개,3개 선택시 남은 갯수가 패턴상
        # 승리패턴인지 패배패턴인지 판단가능
        if(dptable[i-1]==1): tokens.append(0)
        else: tokens.append(1)        

        if(dptable[i-2]==1): tokens.append(0)
        else: tokens.append(1)

        if(dptable[i-3]==1): tokens.append(0)
        else: tokens.append(1)
        
        dptable[i]=max(tokens)

    return dptable[n]

if __name__=="__main__":
    
    n=int(input().strip())

    result=dpMarble(n)

    if(result==1):print('YES')
    else: print('NO')
