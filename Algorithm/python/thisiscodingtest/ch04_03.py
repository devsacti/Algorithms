'''
전통적인 복합알고리즘보단, 다양한 조건을 융합한 구현 문제

여기서 기억할 포인트는,

나라면, 1가지 맵에서 바다는 1로 표기되니, 과거방문지는 -1이나 다른 식으로 표기해서 추후 조건문에서
활용할 생각이었겠지만, 

교재의 경우 별도의 맵_d_를 선언해서 관리함, 일단 따르자.
변수는 허용하는 한 갯수 많게 해서 다양한 조건이나 변형에 대응하기 좋지 않을까함.
'''

def turn_left():
    # 나라면 아규먼트로 받았을 것 같은데, 이런 방법도 알아두자.
    # 개인적인 테스트결과 아규먼트로 받으면, 당연하게도?, 재할당을 통해서 쉘로우 카피의 문제를 피할 수 있다.
    global direction

    direction -=1

    if(direction==-1):
        direction=3

if __name__=='__main__':
    n, m = map(int, input().split())

    #아마도 dimension의 d?
    d=[[0]*m for _ in range(n)]

    x,y,direction= map(int, input().split())

    d[x][y]=1

    #나라면 matrix_map정도였을 것 같은데, 좀더 추상화된듯
    array=[]

    for i in range(n):
        array.append(list(map(int, input().split())))

    dx=[-1,0,1,0]
    dy=[0,1,0,-1]

    # def turn_left():
    #     # 나라면 아규먼트로 받았을 것 같은데, 이런 방법도 알아두자.
    #     # 개인적인 테스트결과 아규먼트로 받으면, 당연하게도?, 재할당을 통해서 쉘로우 카피의 문제를 피할 수 있다.
    #     global direction

    #     direction -=1

    #     if(direction==-1):
    #         direction=3

    count =1
    turn_time=0

    while True:
        turn_left()
        nx=x+dx[direction]
        ny=y+dy[direction]

        if(d[nx][ny]==0 and array[nx][ny]==0):
            d[nx][ny]=1
            x=nx
            y=ny
            count+=1
            turn_time=0
            continue

        else:
            turn_time+=1

        if(turn_time==4):
            nx=x-dx[direction]
            ny=y-dy[direction]

            if(array[nx][ny]==0):
                x=nx
                y=ny
            else:
                break
            turn_time=0

    print(count)
