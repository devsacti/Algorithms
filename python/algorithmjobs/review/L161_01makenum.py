import sys
input=sys.stdin.readline

def dpMakeNum(n):
    if(n>3):dptable=[0]*(1+n)
    else:dptable=[0]*(1+3)

    dptable[1]=1
    dptable[2]=2
    dptable[3]=4
    # an = a_n-1 + a_n-2 + a_n-3
    for i in range(4,n+1):
        dptable[i]=(dptable[i-1]+dptable[i-2]+dptable[i-3])%1000007

    return dptable[n]

if __name__=="__main__":
    n = int(input().strip())
    print(dpMakeNum(n))