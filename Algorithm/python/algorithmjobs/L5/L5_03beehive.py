'''
step1 input

step2
 정육각형은 6개의 삼각형으로 이해가능
 근데 1이 6번 중복 그리고 경계 중복 고려
 ->마름모 3개로 생각하면 제곱꼴 증가와 경계중복 최소화가능
 ->주어진 N보다 같거나 커질때까지 껍질 만들기

'''

if __name__=='__main__':
    N= int(input())

    cnt_beehouses=1

    cnt_peel=1

    while(cnt_beehouses<N):
        cnt_peel+=1
        cnt_beehouses=3*(cnt_peel**2)-3*(cnt_peel)+1
        #print(cnt_peel, cnt_beehouses)

    #print('cnt_peel',cnt_peel)

    print(cnt_peel)