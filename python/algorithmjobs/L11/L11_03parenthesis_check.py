'''
참고로 보니까,
par.en.thesis로 par beside, en in, the put으로 사이에 두다라는 의미로 볼수있다고함

+주어진 괄호가 홀수개면 100프로 NO이긴 한데, 알아만 두자
'''

from collections import deque
import sys

if __name__=="__main__":
    dq_parenthesis_set=deque()
    parenthesis_set=sys.stdin.readline().strip()
    # print(parenthesis_set)
    dq_parenthesis_set=deque(parenthesis_set)
    # print(dq_parenthesis_set)

    stack=deque()
    top_stack=-1

    flag=True

    while(dq_parenthesis_set):
        token=dq_parenthesis_set.popleft()

        if(token=='('):
            stack.append(token)
            top_stack+=1
        else:
            # ')' token 
            # 참고로 이건 어디에 들어갈 토큰이 아님

            #break condtion1 : 처음부터 ')'이면 안됨
            if(top_stack==-1):
                flag=False
                break

            if(stack):
                tmp=stack.pop()
                top_stack-=1
            else:
                #brea condition 2 : stack_bydq에 짝에 맞춰야할 게 없는 경우
                #there is no element for ')', invalid VPS
                flag=False
                break

    #vps면 while 다 돌고,  dq_forstack이 비어져있어야함
    if(stack):
        flag=False

    if(flag==True):
        print('YES')
    else:
        print('NO')
