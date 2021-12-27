from collections import deque

if __name__=="__main__":

    n,m=map(int,input().split())

    dq=deque()
    limit_len_dq=n
    limit_idx_dq=n-1

    cmdlines=[]
    for _ in range(m):
        # print(list_q, front, rear)
        cmdline=input().split()
        # print('cmdline',cmdline)
        cmdlines.append(cmdline)

    for cmdline in cmdlines:
        # print('##',cmdline)
        if(len(cmdline)==2):
            #'1'
            cmd, val=cmdline
            if(len(dq)<limit_len_dq):
                dq.append(val)
            else:
                print('Overflow')
                
        else:
            #'2' popleft '3' print front
            if(cmdline[0]=='2'):
                if(len(dq)>0):
                    # print(list_q[front])
                    tmp=dq.popleft()
                else:
                    print('Underflow')
            else:
                if(len(dq)>0):
                    print(dq[0])
                else:
                    print('NULL')