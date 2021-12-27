
def changer(toN, matrix):
    #print(matrix[toN-1],'end')

    for N in range(toN):
        #print('check')
        for i in range(10):
            if(matrix[N][i] == 0):
                matrix[N][i] = 1
            else:
                matrix[N][i] = 0
        
        for i in range(10):
            if(matrix[i][N] == 0):
                matrix[i][N] = 1
            else:
                matrix[i][N] = 0
        
        #print(*matrix, sep='\n')


    for N in range(toN):
        matrix[N][N]=1
 
    #print('check')
    #print(*matrix, sep='\n')
    return matrix


if __name__ == '__main__':
    toN = int(input())

    matrix = [[0]*10 for i in range(10)]
    #print(matrix[0])
    matrix = changer(toN, matrix)

    for row in matrix:
        # print(list(map(str,row)))
        # for ele in list(map(str,row)):
        #     print(ele,end=' ')

        print(' '.join(map(str,row)))