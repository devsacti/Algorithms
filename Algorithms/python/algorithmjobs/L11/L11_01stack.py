'''
개념은 명확하지만, 구현 중 문법은 아니고 논리 오류로 pop이 안됬음,
중요한 건 이것을 찾기 위해
쓸모없는 짓같은데, print를 다 박아 넣은 것
'''

from collections import deque

if __name__=="__main__":
    n,m=map(int, input().split())

    commands=[]
    stack=deque()

    for i in range(m):
        command=list(map(int,input().split()))
        commands.append(command)

    # print(commands)
    
    for command in commands:
        top=len(stack)-1
        # print(stack, top)

        # print(command)

        #push
        if(len(command)==2):
            if(len(stack)==n):
                print('Overflow')
            else:
                num, val = command
                stack.append(val)
        #pop N top
        else:
            # print('im pop')
            # print(stack, top)

            #내가 빼먹은 부분
            num=command[0]

            if(num==2):
                if(top==-1):
                    print('Underflow')
                else:
                    val_pop=stack.pop()
            else:
                
                if(top==-1):
                    print('NULL')
                else:
                    print(stack[top])
