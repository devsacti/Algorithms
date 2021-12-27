def changer(toN, matrix):
    #print(matrix[toN-1],'end')

    for N in range(toN):
        #print('check')
        for i in range(10):
            if(matrix[N][i] == 0):
                matrix[N][i] = 1
            else:
                matrix[N][i] = 0
        
        '''for i in range(10):
            if(matrix[i][N] == 0):
                matrix[i][N] = 1
            else:
                matrix[i][N] = 0'''
        
        #print(*matrix, sep='\n')
        if(matrix[N][N]==1):
            matrix[N][N]=0
        else:
            matrix[N][N]=1


    # for N in range(toN):
    #     matrix[N][N]=1
 
    #print('check')
    #print(*matrix, sep='\n')
    return matrix

if __name__=='__main__':
    toN = int(input())

    matrix=[]

    for i in range(10):
        row=[]
        matrix.append(list(map(int,input().split())))

    # print('--')
    # for row in matrix:
    #     print(' '.join(map(str,row)))

    matrix = changer(toN, matrix)

    print('--')
    for row in matrix:
        print(' '.join(map(str,row)))

    