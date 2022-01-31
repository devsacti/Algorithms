import sys
import string
from collections import deque

if __name__=="__main__":
    std_str=sys.stdin.readline().strip()
    cur_idx_std=0
    length_std=len(std_str)

    samples=string.ascii_lowercase[:length_std]
    dq_samples=deque(samples)
    # print(dq_samples)

    stack=list()
    top_stack=-1
    top_val='*'

    token_possible=True
    cmds=[]

    while(token_possible):
        std_char=std_str[cur_idx_std]
        # print('cur idx', cur_idx_std,std_char)
        '''possible한 목표가 주어졌을때를 가정한 처리방식 two while'''
        # stack에 채우는 과정, 이후에는 반드시 원하는 값이 맨위에 있거나 그렇지 않을 시 문제
        # 일단 내용물이 있는 경우에 한하여 빼고,
        # 아닌 경우 다른 조건들(문장 완성여부)와 별개로 스탑
        while(std_char!=top_val):
            if(len(dq_samples)>0):
                stack.append(dq_samples.popleft())
                # top을 중심으로 갱신
                top_stack+=1
                top_val=stack[top_stack]
                # print('push')
                cmds.append('push')
            else:
                break

        # 문장 완성 과정 일단 충족하는 동안은 다 뺀다.
        # 이후에는 충족하는 글자는 모두빠지고
        # 스택에는 필요한것과 다른 것이나 비어지거나 등
        while(std_char==top_val):
            tmp=stack.pop()
    
            #top을 중심으로 갱신
            top_stack-=1
            if(top_stack>=0):
                top_val=stack[top_stack]
            else:
                top_val='*'
            # print('pop')
            cmds.append('pop')

            #1개 충족했으니, std_char도 갱신
            cur_idx_std+=1
            if(cur_idx_std<=length_std-1):
                std_char=std_str[cur_idx_std]

        # possible한 목표가 주어졌을때의 break point
        # break 1 : std_str is complete
        # print('2cur idx', cur_idx_std)
        if(cur_idx_std>=length_std):
            break
        '''possible한 목표가 주어졌을때를 가정한 처리방식 two while'''

        '''상위 처리 절차가 완벽하다면, 이 처리절차로 해결되지 않는 케이스를 
        impossible이라고하자'''
        # impossible한 목표가 주어졌을때의 현상
        # break 2 : std_char is under top val
        # 좀더 정확히는 std_char가 top val과는 다르고, 그 아래 있다 라고 정의해야겠지만
        # 위 로직 구조상 조건 충족하면 다 걷어내서, 아래와같이 체크만 하면됨.
        if( std_char in stack):
            token_possible=False
            break

    if(token_possible):
        for cmd in cmds:
            print(cmd)
    else:
        print('impossible')