from collections import deque
import sys
'''
다음에 할때는 기호에서 숫자 변환에 있어서
dict따로 선언해두면 좀더 세련될듯
->do it now

좀더 패턴을 세부분석하면 불필요한 flag=False를 줄일수 있을듯

+중간에 2개의 연속 ()() 또는 []() 등등은 커버되지만,
3개 이상의 경우 현재 if구조로는 불가능하다는 걸 깨닫,
while이 필요.
->여기서부턴 새로운 파일에
'''
def sol_doubleparenthesis(token,topval_stack):
    if(token==')' and topval_stack=='('):
        stack.append( str( int( decimal_token)*2))
    else:
        flag=False
        break

    if(token==']' and topval_stack=='['):
        stack.append( str( int( decimal_token)*3))
    else:
        flag=False
        break

#parenthesis to string num dictionary
precode={
    '()' : '2' , '{}':'3'
}

if __name__=="__main__":
    parenthesis_set=sys.stdin.readline().strip()
    # print(parenthesis_set)
    dq_parenthesis_set=deque(parenthesis_set)
    # print(dq_parenthesis_set)

    stack=list()
    top_stack=-1

    flag=True
    
    sum_point=0

    while(dq_parenthesis_set):
        token=dq_parenthesis_set.popleft()
        # print('cur token',token,end=' ')

        if(token=='(' or token=='['):
            stack.append(token)
            top_stack+=1
            # print('stackin ',stack)
        else:
            # ')' or ']' token 
            
            #break condtion1 : stack의 처음이 ')',']'이면 안됨
            if(top_stack==-1):
                flag=False
                break

            #현재 stack의 top val이 일단 숫자인가 아닌가, 그다음 ( [ 을 판단.
            # 아니다, 숫자들은 다빼네야 2개 3개 이상의 ()()() 등의 꼴을 커버가능
            # 여기서부턴 다른 파이썬 파일에 생성
            topval_stack=stack[-1]

            if(topval_stack.isdecimal()):
                #topval 2 or 3 whatever token is ),]
                #decimal must be poped, and recheck topval
                decimal_token=stack.pop();top_stack-=1
                topval_stack=stack[-1]

                #1개 팝한 뒤, top값이 또 decimal인지 아닌지 체크
                if(topval_stack.decimal()):
                    # again toval is string num
                    # vps and vps, ex ()() []() =>2+2, 3+2
                    operand1=stack.pop();top_stack-=1
                    topval_stack=stack[-1]

                    #at last, checking token
                    if(token==')' and topval_stack=='('):
                        stack.append( str( int( decimal_token)*2))
                    else:
                        flag=False
                        break

                    if(token==']' and topval_stack=='['):
                        stack.append( str( int( decimal_token)*3))
                    else:
                        flag=False
                        break 

                else:
                    # double parenthesis situation,ex (()) => (2)
                    if(token==')' and topval_stack=='('):
                        stack.append( str( int( decimal_token)*2))
                    else:
                        flag=False
                        break

                    if(token==']' and topval_stack=='['):
                        stack.append( str( int( decimal_token)*3))
                    else:
                        flag=False
                        break                    

            else:
                #topval_stack is (  or [
                #and if it is vps there are only two cases; () ,[]
                if(token==')' and topval_stack=='(' ):
                    #
                    oneside=stack.pop()
                    stack.append(precode[oneside+token])
                    # print('out',stack)
                else:
                    #[ with )
                    flag=False
                    break

                if(token==']' and topval_stack=='[' ):
                    oneside=stack.pop()
                    stack.append(precode[oneside+token])
                    # print('out',stack)
                else:
                    #( with ]
                    flag=False
                    break

                #whatever if below line need commonly
                top_stack-=1

    #vps면 while 다 돌고,  dq_forstack이 비어져있어야함
    # print('lastcheck',stack)
    if(stack):
        flag=False

    if(flag==True):
        print('YES')
    else:
        print(0)
