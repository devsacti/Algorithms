'''
ps1.1.

ps1.2.

ps2.1.
bruteforce

ps2.2.

ps3.impl

'''
            

if __name__=='__main__':
    row=5
    col=5
    matrix=[]
    result=[[0]*col for _ in range(row)]

    for i in range(row):
        matrix.append(list(map(int, input().split())))
    
    # print(*matrix,sep='\n')

    for r in range(row):
        for c in range(col):

            # token for checking, per point
            local_minimun=True

            # dir
            dr=[1,-1,0,0]
            dc=[0,0,1,-1]

            for d in range(len(dr)):
                adj_r=r+dr[d]
                adj_c=c+dc[d]

                if(adj_r<0 or adj_r>(row-1) or adj_c<0 or adj_c>(col-1)):
                    continue

                if(matrix[adj_r][adj_c] <= matrix[r][c]):
                    local_minimun=False
            
            if(local_minimun):
                result[r][c]='*'
            else:
                result[r][c]=matrix[r][c]

    # print(*matrix,sep='\n')
    # print(*result,sep='\n')

    for row in result:
        print(' '.join(list(map(str,row))))
