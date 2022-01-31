'''
step1 input, import

step2
 change num to 0 that is same with given cuz to use sum() 같은 오퍼레이터
 였는데 안쓸듯




step3 
 bingoexplorer, chech all row, col, diagonal
 이때 for수를 줄이기 위해 flatten하는 아이디어를 적용해봤는데
 대각선은 어쩔수 없이 이중폴문 쓸라다가 파이썬 컴프리헨션이 떠오름
 그리고 i,j간의 관계파악; i=j or i=5-i

 그런데, 압축적인 만큼 검토에 어려움이 많음....
 멋지게 보단 초라해도 빈틈없이 하자

 방법을 바꾸면서 역시나 또다른 문제를 만났지, 행,열,대각별
 함수에서 1씩 biango를 찾을 때 멈추기 위한 if
 그리고 뒤늦게 이렇게 파트마다 카운팅을 하면 이전에 체크된 열이
 다음 시행에서 또 중복카운팅되서 이르게 멈추는 일이 생김
 또한 파트마다 다음 파트를 위해 지역 매트릭스를 전역변수에 업데이트해줘야
 했는데

 근본적으로 판단의 관점과 threshhold를 바꿔서,
 즉 모든 변화가 ==3이 아니라 >=3꼴형식일때로 관점을 바꾸어
 전역 지역 문제 해결

 추가로 행에서만 빙고가 나오는 등의 문제 발견해서 조정하고
 또 기존 코드 바탕으로 수정하다보니 리턴위치조절을 안해서 오류뜨다가
 재조정

step3(실패작)
def judgebingo(flatten):
    cnt_zero=0
    for n,val in enumerate(flatten,1):
        if(n%5==1):
            cnt_zero=0
        if(val==0):
            cnt_zero+=1
            if(cnt_zero==5):
                return 1
    
    return 0


def bingoexplorer(bingoMatrix,givenNums):

    for n1,givenNum in enumerate(givenNums,1):
        print('n1 ',n1,givenNums[n1-1])
        bingoMatrix_checked=checker(bingoMatrix,givenNum)
        print(*bingoMatrix_checked,sep='\n')
        
        flattenMatrix=sum(bingoMatrix,[])
        print(flattenMatrix)

        tranposedbingMatrix=[list(row) for row in zip(*bingoMatrix)]
        flattentranposedbingMatrix=sum(tranposedbingMatrix,[])
        print(flattentranposedbingMatrix)

        flattendiagonal=[]
        flattendiagonal.extend([bingoMatrix_checked[i][i] for i in range(5)])
        flattendiagonal.extend([bingoMatrix_checked[i][4-i] for i in range(5)])
        print(flattendiagonal)
        print()

        bingo=0
        cnt_bingo=0

        #행단위 빙고 체크
        bingo=judgebingo(flattenMatrix)
        cnt_bingo+=bingo
        
        #열단위 빙고 체크
        bingo=judgebingo(flattentranposedbingMatrix)
        cnt_bingo+=bingo
        #대각선 빙고 체크
        bingo=judgebingo(flattendiagonal)
        cnt_bingo+=bingo

        if(cnt_bingo==3):
            print(n1)
            break

'''

'''step2'''
def checker(bingoMatrix,givenNum):
    for row in bingoMatrix:
        if(givenNum in row):
            row[row.index(givenNum)]=0

    return bingoMatrix


'''step3'''
def rowbingocounter(bingoMatrix):
    cnt_row_bingo=0
    for row in bingoMatrix:
        if(sum(row)==0):
            cnt_row_bingo+=1

    return cnt_row_bingo

def colbingocounter(bingoMatrix):
    transposedMatrix=[list(row) for row in zip(*bingoMatrix)]
    cnt_col_bingo=0

    for row in transposedMatrix:
        if(sum(row)==0):
            cnt_col_bingo+=1

    return cnt_col_bingo

def diagonalbingocounter(bingoMatrix):
    diagonalline=[]
    diagonalline.append([bingoMatrix[i][i] for i in range(5)])
    diagonalline.append([bingoMatrix[i][4-i] for i in range(5)])

    cnt_diagonal_bingo=0

    for line in diagonalline:
        if(sum(line)==0):
            cnt_diagonal_bingo+=1

    return cnt_diagonal_bingo

def bingoexplorer(bingoMatrix,givenNums):

    for n1,givenNum in enumerate(givenNums,1):
        cnt_bingo=0
        #print('n1 ',n1,givenNums[n1-1])
        bingoMatrix_checked=checker(bingoMatrix,givenNum)
        #print(*bingoMatrix_checked,sep='\n')

        cnt_bingo+=rowbingocounter(bingoMatrix_checked)
        #print(cnt_bingo)
        cnt_bingo+=colbingocounter(bingoMatrix_checked)
        #print(cnt_bingo)
        cnt_bingo+=diagonalbingocounter(bingoMatrix_checked)
        #print(cnt_bingo)

        if(cnt_bingo>=3):
            print(n1)
            break

if __name__=='__main__':
    N=5

    bingoMatrix=[]

    for i in range(N):
        bingoMatrix.append(list(map(int, input().split())))

    givenNums=[]

    for i in range(N):
        givenNums.extend(list(map(int, input().split())))

    
    #print(*bingoMatrix,sep='\n')

    #print(givenNums)

    '''step3'''
    bingoexplorer(bingoMatrix,givenNums)

