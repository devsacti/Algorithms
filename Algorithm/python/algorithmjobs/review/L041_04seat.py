import sys

def robot( init_r, init_c ):
    global matrix
    global R,C,K

    flag=1

    matrix[init_r][init_c]=flag
    flag+=1

    mag=1
    dr=[0,mag,0,-mag]
    dc=[mag,0,-mag,0]

    d=0
    cnt_trial=R*C
    token_possible=True
    while(flag<=cnt_trial):
        cand_r=init_r+dr[d]
        cand_c=init_c+dc[d]

        if(cand_r<0 or cand_r>(R-1) or cand_c<0 or cand_c>(C-1)):
            d=(d+1)%4
            cand_r=init_r+dr[d]
            cand_c=init_c+dc[d]

        if(matrix[cand_r][cand_c] != 0):
            d=(d+1)%4
            cand_r=init_r+dr[d]
            cand_c=init_c+dc[d]

        init_r=cand_r
        init_c=cand_c

        matrix[init_r][init_c]=flag

        if(flag==K):
            print( init_r+1 , init_c+1 )
            break

        flag+=1

    # 다돌고 난뒤,
    if(K>flag):
        print(0)


if __name__=="__main__":
    R,C = map(int, sys.stdin.readline().split())
    K = int(sys.stdin.readline().strip())

    matrix=[[0]*C for _ in range(R)]

    robot(0,0)

    # print(*matrix, sep='\n')

