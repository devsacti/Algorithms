'''
step1
이전 작동시기에 k광년을 이동하였을 때,
next choices K-1 or k+1

예를 들어, 이 장치를 처음 작동시킬 경우 -1 , 0 , 1 광년
1 move 그 다음에는 0 , 1 , 2 
 1 move 0 1 2; again
 2 move 다음 시기엔 1, 2, 3
   1
   2
   3 move

y지점에 도착하기 바로 직전의 이동거리는 반드시 1광년
현재 위치 x 와 목표 위치 y
0 ≤ x < y ≤ 100,000,000

!필요한 최소한의 공간이동 장치 작동 회수를 출력

tablet의
L5_12 그림 참고, 결국은 귀납적인 접근해결임,
이동횟수가 가질수 있는 여러패턴들 중에서도 최대 이동거리 값들을
모아서 만든 수열을 도출하면 됨

참고로 4회 이동시 가지는 패턴은 대략 4개이고 이 패턴들 중 최대 이동거리는 6이다.
근데, y가 5칸뒤라면 몇 회이동해야?
3회이동시 최대이동거리보단 크므로
4회로 올라가는 판단하게 짜면 된다.

step2
 주어진 조건을 컴퓨터과학적 변수로 치환, 좌표->리스트
 표식을 통해 우주선이나 종착지 위치 표현

 그 표식에 따라서 알고리즘 작성
 만약 이동가능구간 내에 목표지점이 없으면 최대한 멀리
  이동가능구간 정의, 탐색 과정 정의
 아니면 목표지점으로

if __name__=='__main__':
    x,y=map(int, input().split())

    #참고로 x,y는 성질상 idx니까 내 습관에 따라
    idx_x=x
    idx_y=y

    path=[0]*(idx_y-(idx_x))
    len_path=(idx_y-(idx_x))

    # print(path)
    # print(len_path)

    #tablet으로 도출한 수열을 만들자.
    #초기값
    #내 생각의 편의를 위해 아래 수열의 idx는 이동횟수에 대응한다.
    # 0번은 없으니 0, 1번은 1, 2번은 2
    # 그리고 앞으로 3번이동이 가질수 있는 최대이동거리가 추가된다.
    # 0 1 2 4 6 9 12 등등, +2가 두번, +3이 두번, 그리고 +4가 두번이 예상된다.
    seq_maxdist_permove=[0,1,2]

    differenceterm=2
    #seq_maxdist_permove의 마지막값이 path보다 크거나 같아서 횟수판별될때까지
    #계차항 1번 사용시 토큰값이 감소해서 다 쓰면 계차항 +1하게, lifespan of difference term
    lifespan_differ_term=2
    
    #수열의 다음 항을 계산해서 추가한다.
    while(seq_maxdist_permove[-1]<len_path):
        
        #아직 현 differ_term을 써도되거나 아니거나
        if(lifespan_differ_term>0):
            curlast_term=seq_maxdist_permove[-1]
            seq_maxdist_permove.append(curlast_term+differenceterm)
            lifespan_differ_term-=1
        else:
            #계차 리뉴얼과 업데이트
            differenceterm+=1
            lifespan_differ_term=2

            curlast_term=seq_maxdist_permove[-1]
            seq_maxdist_permove.append(curlast_term+differenceterm)
            lifespan_differ_term-=1

    # print(seq_maxdist_permove)
    #다행히 while의 처리로직상 따로 주어진 거리가 어느 인덱스에 연결되야할지
    # 따로 판단안하고, 마지막 인덱스만 출력하면됨
    print(len(seq_maxdist_permove)-1)

+이렇게 했더니, 80점 뜨고 나머지는 메모리아웃뜸, 최대거리를 좀더
효과적으로 구해야할듯

일단 쓸모없는 path빼고,
나중에 len(seq_maxdist_permove)로 부하 생길거같은거 뺏떠니,
100~~~~~~~~점.
'''

if __name__=='__main__':
    x,y=map(int, input().split())

    #참고로 x,y는 성질상 idx니까 내 습관에 따라
    idx_x=x
    idx_y=y

    '''메모리리밋땜시 자잘한 할당도 out'''
    # path=[0]*(idx_y-(idx_x))
    len_path=(idx_y-(idx_x))

    # print(path)
    # print(len_path)

    #tablet으로 도출한 수열을 만들자.
    #초기값
    #내 생각의 편의를 위해 아래 수열의 idx는 이동횟수에 대응한다.
    # 0번은 없으니 0, 1번은 1, 2번은 2
    # 그리고 앞으로 3번이동이 가질수 있는 최대이동거리가 추가된다.
    # 0 1 2 4 6 9 12 등등, +2가 두번, +3이 두번, 그리고 +4가 두번이 예상된다.
    seq_maxdist_permove=[0,1,2]
    max_idx_seq=2

    differenceterm=2
    #seq_maxdist_permove의 마지막값이 path보다 크거나 같아서 횟수판별될때까지
    #계차항 1번 사용시 토큰값이 감소해서 다 쓰면 계차항 +1하게, lifespan of difference term
    lifespan_differ_term=2
    
    #수열의 다음 항을 계산해서 추가한다.
    while(seq_maxdist_permove[-1]<len_path):
        
        #아직 현 differ_term을 써도되거나 아니거나
        if(lifespan_differ_term>0):
            curlast_term=seq_maxdist_permove[-1]
            seq_maxdist_permove.append(curlast_term+differenceterm)
            #term add, idx increase
            max_idx_seq+=1

            lifespan_differ_term-=1


        else:
            #계차 리뉴얼과 업데이트
            differenceterm+=1
            lifespan_differ_term=2

            curlast_term=seq_maxdist_permove[-1]
            seq_maxdist_permove.append(curlast_term+differenceterm)
            #term add, idx increase
            max_idx_seq+=1

            lifespan_differ_term-=1

    # print(seq_maxdist_permove)
    # 다행히 while의 처리로직상 따로 주어진 거리가 어느 인덱스에 연결되야할지
    # 따로 판단안하고, 마지막 인덱스만 출력하면됨
    print(max_idx_seq)
