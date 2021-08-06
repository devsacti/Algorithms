import sys

# 해설도 나랑 다른 스텝을 하진 않았음, 다만, 숫자 지울때마다 가로세로대각 체크가 아니라
# 일종에 전체 숫자 지우는 과정을 총 3세번하는데, 그때 각 테스트마다 가로, 세로, 대각을 체크하는 방식임

# 한편 빙고체크판 따로 선언하니까 좋은점은, 'x'대신 1같은걸로 조건을 수식화하기 편한듯
# 물론 따로 빙고체크판 없어도, 'x'대신 -1 같은 거 넣고 sum 결과가 -5인 경우로 하면 되긴하는데
# 연상 용이한 건 전자인듯

# 한편 여기서 문제는 bing수가 누적이 되는걸 방지되게 초기화해야함

# 한편, 대각선 체크를 '한번에' 좌상 우하 와 우상 좌하 체크하니까 둘 중 1개만 되도
# 뱉어야할때 

# 한번 1 체크했더니 빙고 수가 +1이 아니라 +2인경우 발생, 오목에서 33처럼,
# 이런 경우 판단을 위해 ==3이 아니라 >=3

def checker_row(ck_matrix):
    global cnt_rowbingo
    cnt_rowbingo=0

    for row in ck_matrix:
        if(sum(row)==5):
            cnt_rowbingo+=1


def checker_col(ck_matrix):
    global cnt_colbingo
    cnt_colbingo=0

    transposed=list(zip(*ck_matrix))
    for symbol_col in transposed:
        if(sum(symbol_col)==5):
            cnt_colbingo+=1

def checker_diagonal(ck_matrix):
    global cnt_diagonalbingo
    cnt_diagonalbingo=0

    diag1=[(i,i) for i in range(N)]
    diag2=[(i,4-i) for i in range(N)]

    val1=[]
    val2=[]
    for co in diag1:
        idx_r=co[0]
        idx_c=co[1]
        val1.append(ck_matrix[idx_r][idx_c])

    for co in diag2:
        idx_r=co[0]
        idx_c=co[1]
        val2.append(ck_matrix[idx_r][idx_c])

    if(sum(val1)==5):
        cnt_diagonalbingo+=1
    if(sum(val2)==5):
        cnt_diagonalbingo+=1


if __name__=="__main__":
    cnt_rowbingo=0
    cnt_colbingo=0
    cnt_diagonalbingo=0

    N,M = 5,5 

    matrix=[]
    ck_matrix=[[0]*M for _ in range(N)]
    for _ in range(N):
        row=list(map(int,sys.stdin.readline().split()))
        matrix.append(row)

    nums=[]

    for _ in range(N):
        row=list(map(int,sys.stdin.readline().split()))
        nums.extend(row)

    # print(*matrix,sep='\n')
    # print(nums)

    token_break1=False
    token_break2=False
    token_break3=False


    for ri,num in enumerate(nums,1):

        for idx_r in range(N):
            for idx_c in range(M):
                if(matrix[idx_r][idx_c]==num):
                    ck_matrix[idx_r][idx_c]=1
                    #per num,
                    # check row, col, diagonal
                    # print(num)
                    # print(*ck_matrix,sep='\n')

                    checker_row(ck_matrix)
                    checker_col(ck_matrix)
                    checker_diagonal(ck_matrix)

                    # print('#',cnt_rowbingo+cnt_colbingo+cnt_diagonalbingo)
                    if(cnt_rowbingo+cnt_colbingo+cnt_diagonalbingo>=3):
                        # print(*ck_matrix,sep='\n')
                        print(ri)
                        token_break1=True
                        break
            if(token_break1):
                token_break2=True
                break
        
        if(token_break2):
            break


        
