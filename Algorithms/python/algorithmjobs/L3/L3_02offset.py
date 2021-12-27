from collections import deque

def getArgs():
    #N, S = map(int,input().split())
    row=5
    matrix=[]

    for i in range(row):
        matrix.append(list(map(int, input().split())))
    
    return matrix

def movechange(std,idx_std, matrix):
    dr=[-1,1,0,0]
    dc=[0,0,-1,1]

    peripheralvals=[]

    for i in range(4):
        idx_r=idx_std[0]+dr[i]
        idx_c=idx_std[1]+dc[i]

        if(idx_r<0 or idx_r>4 or idx_c<0 or idx_c>4):
            continue
        else:
            peripheralvals.append(matrix[idx_r][idx_c])

    #print(peripheralvals)
    checkcnt=len(peripheralvals)

    for item in peripheralvals:
        if(item=='*'):
            continue
        elif(item-std>0):
            checkcnt-=1
        else:
            continue
    
    if(checkcnt==0):
        matrix[idx_std[0]][idx_std[1]]='*'

    print(matrix[idx_std[0]][idx_std[1]],end=' ')

    return matrix


def makeMarker(matrix):
    row=len(matrix)
    col=len(matrix[0])

    #관련 컴프리헨션
    #[ (x, y) for x in ['쌈밥', '치킨', '피자'] for y in ['사과', '아이스크림', '커피']]

    for idx_row in range(row):
        for idx_col in range(col):
            std=matrix[idx_row][idx_col]
            idx_std= [idx_row,idx_col]

            movechange(std,idx_std,matrix)

        print()

    #print(*matrix,sep='\n')
            

if __name__=='__main__':
    matrix = getArgs()
    #print(*seqs,sep='\n')
    makeMarker(matrix)
