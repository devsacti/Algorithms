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

def aggregate_subsum(stack,top_stack):
    tmp_list=list()
    # print(stack, stack[top_stack],type(stack[top_stack]),stack[top_stack].isdecimal())    
    while(top_stack>=0 and stack[top_stack].isdecimal()):
        # print('ck')
        tmp_list.append(int(stack.pop()))
        top_stack-=1
    parent_sum=sum(tmp_list)
    stack.append(str(parent_sum))
    top_stack+=1

    return stack,top_stack


#parenthesis to string num dictionary
# i was going to () to int 2, but to use isdecimal(), so str '2'
precode={
    '()' : '2' , '[]':'3'
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
            stack.append(token);top_stack+=1
            # print('stackin ',stack,'top ',top_stack)
        else:
            # ')' or ']' token 
            
            # 숫자들은 다빼네야 3개 이상의 ()()() 등의 꼴을 커버가능
            sub_sum=0
            list_nums=list()
            while(top_stack>=0 and stack[-1].isdecimal()):
                list_nums.append(int(stack.pop()))
                top_stack-=1
            # given rule, anyway all elements_ 22233  from  ()()()[][]_
            # should be added, so sum
            sub_sum=sum(list_nums)
            # print('stackout, sub_sum',sub_sum,end=' ')

            # break condtion1 : 숫자 거둬내고 stack이 비어진 상태로
            # ')',']'이 push되거나 연산되서는 안됨
            if(top_stack==-1):
                flag=False
                # print('ck1')
                break
            else:

                if(sub_sum==0):
                    # 대표적으로 스택에 좌 편만 있는 경우,
                    # 빈스택은 72행에서 방지하고, 그 상위 ifelse에서 (랑 [ 추가된 상황
                    
                    # desirable situation are only () or []
                    topval_stack=stack.pop();top_stack-=1
                    # print(token, topval_stack,end='/')
                    if(token==')' and topval_stack=='('):
                        stack.append(precode[topval_stack+token]);top_stack+=1

                    elif(token==']' and topval_stack=='['):
                        stack.append(precode[topval_stack+token]);top_stack+=1
                    else:
                        flag=False
                        # print('ck3')
                        break
                    # print('sub sum in',stack)

                else:
                    # duplication of parenthesis like (8) from (()[][])
                    # sub sum is int 8
                    topval_stack=stack.pop();top_stack-=1

                    # print(token, topval_stack,end='/')
                    if(token==')' and topval_stack=='('):
                        # '2'-> 2, 2*8, '16', pushing '16'
                        stack.append( str(int(precode[topval_stack+token])*sub_sum) );top_stack+=1
                    elif(token==']' and topval_stack=='['):
                        stack.append( str(int(precode[topval_stack+token])*sub_sum) );top_stack+=1
                    else:
                        flag=False
                        # print('ck5')
                        break
                    # print('sub sum in',stack,'and top', top_stack)

    #after calcul sub sum, we need to aggregate sub sum
    stack,top_stack=aggregate_subsum(stack,top_stack)
    # 
    # after last pop, there is no element in stack
    candi_sum_point=stack.pop()
    # print('\nlastcheck',stack,candi_sum_point,type(candi_sum_point))
    # print(candi_sum_point.isdecimal())
    if(stack):
        flag=False

    if(flag==True and candi_sum_point.isdecimal()==True):
        print(int(candi_sum_point))
    else:
        print(0)
