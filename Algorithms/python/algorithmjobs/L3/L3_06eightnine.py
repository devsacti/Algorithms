if __name__=='__main__':
    N,M = map(int,input().split())
    
    matrix=[]

    for i in range(N):
        row=list(map(int, input().split()))
        matrix.append(row)
    
    #print(*matrix,sep='\n')

    for i in range(N):
        for j in range(M-1,-1,-1):
            print(matrix[i][j],end=' ')
        print()

