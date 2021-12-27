'''
참고로 보니까,
par.en.thesis로 par beside, en in, the put으로 사이에 두다라는 의미로 볼수있다고함

+주어진 괄호가 홀수개면 100프로 NO이긴 한데, 알아만 두자

+코드에 오류_stack_bydq에서 popleft가 아니라 pop을 해야하는데_
에도 불구 100점 나옴, 케이스들이 운좋게 1개 들어오면 바로 1개 나가야하는 상황이라
그랬던듯

정상답안은 L11_03parenthesis_check임
한편, 대책으로
stack은 리스트
원형큐는 deque로 선언하자
'''

from collections import deque
import sys

if __name__=="__main__":
    dq_parenthesis_set=deque()

    # 문제에서 주어진 시간이 매우 짧은 코테의 경우,
    # input()은 받는것만으로 시간초과발생한다함
    # parenthesis_set=list(input())

    #아래와같이 하면 '문자열'과 독립된 '\n'이 들어옴
    # print(sys.stdin.readline())
    # 확인용
    # print(list(sys.stdin.readline()))

    # \n을 제거하는 방법은 여러 변환에 걸쳐서 다양한데
    # 일단 strip 그다음 split으로 결정,
    #  split은 abcd\n을 '마치' ['abcd','\n']으로 쪼갠 뒤 마지막 항을 빼는 거라
    # ['abcd']가 리턴됨

    parenthesis_set=sys.stdin.readline().strip()
    # print(parenthesis_set)
    dq_parenthesis_set=deque(parenthesis_set)
    # print(dq_parenthesis_set)

    stack_bydq=deque()
    top_stack=-1

    flag=True

    #python 강점,!! if도 동일
    # 아래상황에서 deque는 bool값을 리턴하는데
    # item이 1개라도 있다면 True 아니라면 False리턴한다고함, 아마도 len기반일듯
    while(dq_parenthesis_set):
        token=dq_parenthesis_set.popleft()

        if(token=='('):
            stack_bydq.append(token)
            top_stack+=1
        else:
            # ')' token 
            # 참고로 이건 어디에 들어갈 토큰이 아님

            #break condtion1 : 처음부터 ')'이면 안됨
            if(top_stack==-1):
                flag=False
                break

            if(stack_bydq):
                tmp=stack_bydq.popleft()
                top_stack-=1
            else:
                #brea condition 2 : stack_bydq에 짝에 맞춰야할 게 없는 경우
                #there is no element for ')', invalid VPS
                flag=False
                break

    #vps면 while 다 돌고,  dq_forstack이 비어져있어야함
    if(stack_bydq):
        flag=False

    if(flag==True):
        print('YES')
    else:
        print('NO')
