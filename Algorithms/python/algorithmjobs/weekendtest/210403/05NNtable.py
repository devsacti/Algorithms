# NN단표

import sys

if __name__=="__main__":
    N=int(sys.stdin.readline().strip())
    K=int(sys.stdin.readline().strip())

    matrix=[]
    for i in range(N):
        row=[(i+1)*n for n in range(1,N+1)]
        matrix.append(row)

    # print(matrix)
    cands=[num for num in range(1,N*N+1)]
    print(cands)

    idx_left=0
    idx_right=N*N-1
    while(idx_right-idx_left>=0):
        idx_mid=int((idx_right+idx_left)/2)

        val=cands[idx_mid]

        cnt_inmatrix=0
        for num_row in range(1,N+1):
            cnt_inmatrix+=val//num_row
        
        if(cnt_inmatrix==K):
            print(val)