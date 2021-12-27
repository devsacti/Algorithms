# 괄호의 값

import sys
from collections import deque

precode={
    '()' : '2', '[]': '3'
}

if __name__=="__main__":
    parenthesis_set=sys.stdin.readline().strip()
    dq_parenthesis_set=deque(parenthesis_set)

    stack=list()
    top_stack=-1
    val_top='*'


    token_possible=True
    while(token_possible):
        cur_item=dq_parenthesis_set.popleft()
        # print('---#',stack, top_stack)
        # print('---#',cur_item)
        
        if(cur_item=='(' or cur_item=='['):
            stack.append(cur_item)

            top_stack+=1
            val_top=stack[top_stack]
            # print('after insert ',stack ,top_stack)
            # print()
        else:
            # val_top :  (, [ ,decimal, *  cur item are only ) or ]
            # print('## top and cur ',vals_top , cur_item)

            if(val_top.isdecimal()):
                # print('##deci', val_top)

                tmp_list=[]
                while(val_top.isdecimal()):
                    tmp_list.append(int(stack.pop()))

                    top_stack-=1
                    if top_stack == -1:
                        val_top='*'
                    else:
                        val_top=stack[top_stack]
                
                val_between=str(sum(tmp_list))
                # print('#### after while ', stack, top_stack)

                # if possible input, the acceptables are only () ,[]
                if(val_top+cur_item == '()' or val_top+cur_item == '[]'):
                    val_top=stack.pop()
                    stack.append( str( eval(precode[val_top+cur_item]+'*'+val_between)))
                    #top stack은 +-1로 변화없고, val top만 갱신
                    val_top=stack[top_stack]
                else:
                    # *), *], [) ,(]
                    token_possible=False
                    break

            else:
                # val top is not decimal ; ( , [ , *
                # print('##not deci', val_top)

                # !! if input was possible parenthesis,
                # cur item can be only ) or ]
                # results are only () or []
                # !! if not possible, that means False input, and 0
                if(val_top+cur_item == '()' or val_top+cur_item == '[]'):
                    val_top=stack.pop()
                    stack.append(precode[val_top+cur_item])

                    #top stack은 +-1로 변화없고, val top만 갱신
                    val_top=stack[top_stack]
                    # print('after parenthesis to int ',stack)
                else:
                    token_possible=False
                    break

        if(len(dq_parenthesis_set)==0):
            break

    # print(stack)
    
    ## 로직상 ( [ 은 제한없이 받는중,
    # 그렇다고 괄호의 갯수가 짝수여야하고, 최대 스택에는 그 짝수의 절반까지가 유효하다는
    # 법칙이 있지만 모든 오류를 걷어내지 못하여 부득이 아래와 같이 무제한 입력을 제한
    if( '(' in stack or '[' in stack):
        token_possible=False

    if(token_possible):
        print(sum(map(int,stack)))
    else:
        print(0)