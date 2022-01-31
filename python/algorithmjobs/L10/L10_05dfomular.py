'''
점화식; 뉴턴 근사법
fx가 주워지고 그 도함수도 특정가능해서 사용가능

'''
if __name__=='__main__':
    a=int(input())

    # x**2+x==a
    # x**2+x-a=0
    # 2*x+1 

    x1=100
    x2=x1-(x1**2+x1)/(2*x1+1)

    while(abs(x2-x1)>=1):
        # print(x1, x2)
        x1=x2
        x2=x1-(x1**2+x1-a)/(2*x1+1)

    # print(x2)
    print(int(x2))

