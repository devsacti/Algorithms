'''
step1 input and make matrix and val

step2 makejudgement

'''

def makejudgement(matrix, idx_r, idx_c):
    dr=[-1,1,0,0,1,1,-1,-1]
    dc=[0,0,-1,1,-1,1,-1,1]

    cnt_mine=0

    if(matrix[idx_r][idx_c]==1):
        print('game over')
    else:
        for i in range(len(dr)):
            idx_movedr=idx_r+dr[i]
            idx_movedc=idx_c+dc[i]
            #print(matrix[idx_movedr][idx_movedc])

            if(matrix[idx_movedr][idx_movedc]==1):
                cnt_mine+=1

        print(cnt_mine)

    
if __name__=='__main__':
    N, M = map(int, input().split())

    X,Y = map(int, input().split())

    idx_r, idx_c = X-1, Y-1

    #12번 문제에서 혼동했던 문법상 N,M 위치 혼동 또 발생
    #이 문제풀이와 무관하지만 재강조를 위해 남김

    #matrix=[[0]*M for i in range(N)]
    #print(*matrix, sep='\n')


    matrix=[]

    for i in range(N):
        matrix.append(list(map(int, input().split())))

    #print(*matrix, sep='\n')

    '''step 2'''

    makejudgement(matrix,idx_r, idx_c)




    


