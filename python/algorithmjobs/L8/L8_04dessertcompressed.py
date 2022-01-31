'''
시간 초과 대응 압축형
.의 갯수가 일정 수준 넘어가면 어짜피 무용지물 인걸 해결해보자
+그냥 계산기 쓰자

+계산기가 더 시간 오래 걸림
'''
from collections import deque
import time

def postfixeval(list_postfix):
    global cnt
    valStack=deque()

    for token in list_postfix:

        if token.isdecimal():
            valStack.append(int(token))
        
        elif token == '+':
            operand1=int(valStack.pop())
            operand2=int(valStack.pop())
            valStack.append(operand2+operand1)
        
        elif token == '-':
            operand1=int(valStack.pop())
            operand2=int(valStack.pop())
            valStack.append(operand2-operand1)

        elif token == '.':
            operand1=str(valStack.pop())
            operand2=str(valStack.pop())
            # print(operand2+operand1)
            valStack.append(int(operand2+operand1))
    
    # print(valStack.pop())
    sum=valStack.pop()
    if(sum==0):
        cnt+=1
        return 1
    else:
        return 0

#precoding?
prec ={
    '.' : 2 , '+' : 1, '-' : 1
}

def infix2postfix(infix):
    opStack=deque()
    list_postfix=list()
    # print(infix)
    for element in infix:
        # print(element)
        if(element.isdecimal()):
            list_postfix.append(element)
            # print('#',list_postfix, opStack)
        else:
            # print(len(opStack))
            if(len(opStack)!=0):

                while(len(opStack)>0):
                    val_top=opStack[-1]
                    if(prec[val_top]>=prec[element]):
                        list_postfix.append(opStack.pop())
                    else:
                        break
                
                opStack.append(element)

            else:
                opStack.append(element)
            # print('#',opStack)

    while(len(opStack)>0):
        list_postfix.append(opStack.pop())
    # print('#',list_postfix)

    token_eval=postfixeval(list_postfix)

    return token_eval

def operator(depth, result, limit):
    global nums
    global cnt
    
    if(depth==limit):
        # print(result)
        cnt_punctuation=result.count('.')
        
        if(cnt_punctuation>limit/2):
            pass
        else:
            infix=list()

            for idx in range(n-1):
                infix.append(nums[idx])
                infix.append(result[idx])
            infix.append(nums[-1])
            # print(' '.join(infix))

            #원래라면 infix지만 운좋게 그 원소들이 성질별로 쪼개져있으니, 이거 활용
            # 할라고 했는데, 해보니까 인덱스 처리가 까다로워서 원래로
            token_sum=infix2postfix(infix)
            # print(token_sum)
            if(token_sum==1 and cnt<=20):
                print(' '.join(infix))

            
    else:
        for element in ('+','-','.'):
            result[depth]=element
            operator(depth+1, result,limit)
            result[depth]=0

if __name__=="__main__":
    start=time.time()
    global n
    n=int(input())

    global nums
    nums=[str(i) for i in range(1,n+1)]
    # print(nums)

    global cnt
    cnt=0


    depth=0
    result=[0]*(n-1)
    limit=(n-1)
    
    operator(depth,result,limit)
    print(cnt)
    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
    