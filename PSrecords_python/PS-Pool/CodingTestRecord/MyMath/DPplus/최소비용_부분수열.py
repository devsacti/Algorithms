import sys
input=sys.stdin.readline
# 연속구간으로 구매하는 방식이라면, 특정 윈도우 내에서 물건을 사고
#  남은 상품들에 대해서 1개씩 사는 것보단, 구간단위로 사는 것이 당연히 저렴하다.
# 1개씩 사면 반드시 다 제값이지만, 일단 구간 내 넣으면 최대값만 지불하면 주변값이 들어오니까
# 그렇다면, 내가 특정인덱스까지를 윈도우의 한계로 잡을 때
# 남은 상품들은 당연히 윈도우 단위로 사는게 현명하고, 정확히는 끝부분까지 사는 게 현명하다.
# 결과적으로 특정 인덱스를 기준으로 현재 살 1번째 윈도우 영역과
# 남은 상품들로 구분된 2번째 윈도우가 존재한다.
# 그것의 합의 최솟값을 구해보자.

def dp(costs,cnts):
    length=len(costs)
    # 1th window
    dptable=[0]*length
    # 2th window
    dptable2=[0]*length

    # integration of dptables
    dptable3=[0]*length

    #init
    dptable[0]=costs[0]*cnts[0]
    dptable2[0]=max(costs[0+1:])*max(cnts[0+1:])
    dptable3[0]=dptable[0]+dptable2[0]
    
    # calcul only dptable during making longest increasing sequence
    for idx in range(1,length):
        print(idx)
        items=costs[:idx+1]
        items2=cnts[:idx+1]
        print(items,items2)
        
        items3=costs[idx+1:]
        items4=cnts[idx+1:]
        print(items3,items4)
        if(items3==[]):items3.append(0)
        if(items4==[]):items4.append(0)

        dptable[idx]=max(items)*max(items2)
        dptable2[idx]=max(items3)*max(items4)

        dptable3[idx]=dptable[idx]+dptable2[idx]

        print(dptable)
        print(dptable2)
        print('--')

    print(dptable3)
    print(min(dptable3))

if __name__=="__main__":
    costs=list(map(int,input().split()))
    cnts=list(map(int,input().split()))

    dp(costs,cnts)