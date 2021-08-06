from collections import deque
# 문제 요구는 원시 큐,
# 내가 상정한건 deque기반 원형큐

if __name__=="__main__":
    n,m=map(int,input().split())

    front=0
    rear=0

    list_q=[-1]*n
    limit_idx_q=n-1

    cmdlines=[]
    for _ in range(m):
        # print(list_q, front, rear)
        cmdline=input().split()
        # print('cmdline',cmdline)
        cmdlines.append(cmdline)
    # print()

    for cmdline in cmdlines:
        # print('##',cmdline)
        if(len(cmdline)==2):
            #'1 1'
            cmd, val=cmdline
            if(rear<=limit_idx_q):
                list_q[rear]=val
                #deque면 아래행 없어야겠는데, 여기는 아니니 일관성상 냅둠
                rear+=1
            else:
                print('Overflow')
        else:
            #'2' popleft '3' print front
            if(cmdline[0]=='2'):
                # underflow means there is nothing to dequeue
                # case 1, init situation, front==0==rear
                # case 2,
                # enqueue, front==0, rear==1
                # dequeue, front==1, rear==1
                if(front==rear):
                    print('Underflow')
                else:
                    # print(list_q[front])
                    front+=1
            else:
                # case1 init situation
                # case2 enqueue, dequeue, ex front == 1 and rear ==1
                if(front==rear):
                    print('NULL')
                else:
                    print(list_q[front])
                    

