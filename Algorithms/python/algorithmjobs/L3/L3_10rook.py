#import pprint
'''
step1. input
step2. find idx and range_rook
#step2f1
#step2f2
step3. check 1 is at range of rook
step4. check 3 is blocking

'''
def findrook(matrix):
    idxs_rook=[]

    # idx_row=0
    # for row in matrix:
    #     if(row.index(2) is not None):
    #         idxs_rook.append(row.index(2))
    #     else:
    #         continue
    #     idx_row+=1
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j]==2):
                idxs_rook.append( [i,j] )

    #print(idxs_rook)
    return idxs_rook

def step3(idxs_rook, matrix):
    # idxs_rook ; [[],[]]
    idxs_row=[]
    idxs_col=[]
    for idx in idxs_rook:
        idxs_row.append(idx[0])
        idxs_col.append(idx[1])

    for idx_row in idxs_row:
        for element in matrix[idx_row]:
            if(element==1):
                return [idx_row, matrix[idx_row].index(1)]
    for idx_col in idxs_col:
        for i in range(len(matrix)):
            if(matrix[i][idx_col]==1):
                return [i, idx_col]
    
    return [-1,-1]


def step4(step3,matrix):
    if(step3==[-1,-1]):
        print('0')
    else:
        #rook들의 좌표들을 기준으로 1을 찾으면 복잡하니
        #1의 좌표를 기준으로 3이 블로킹중인지 보자
        #이제야 생각해보니 룩들의 좌표값은 필요없고
        #그냥 1기준으로 4방면 체크할수도 있었다.
        #이때는 이때대로 또 체크할사항이 생겼겠지만 더 쉬웠을듯

        idx_row, idx_col=step3

        lefts=list() 
        rights=list()
        downs=list()
        ups=list()

        #아래는 check용 append()
        for idx in range(idx_col,-1,-1):
            lefts.append(matrix[idx_row][idx])

        for idx in range(idx_col,8):
            rights.append(matrix[idx_row][idx])

        for idx in range(idx_row,-1,-1):
            ups.append(matrix[idx][idx_col])

        for idx in range(idx_row, 8):
            downs.append(matrix[idx][idx_col])
            
        #print(lefts, rights, downs, ups)
        fourways=[lefts,rights,downs,ups]

        cnt_blocking=0
        life_king=1
        # for way in fourways:
        #     if(2 in way):
        #         if(3 in way):

        #     else:
        #         continue

        for way in fourways:
            for element in way:
                if(element==3):
                    cnt_blocking+=1
                    #r공격기회가 1번이라 블록은 1이면 끝
                elif(element==2):
                    if(cnt_blocking==0):
                        life_king-=1
                        cnt_blocking-=1
                else:
                    continue
            cnt_blocking=0

        if(life_king==1):
            print('0')
        else:
            print('1')

if __name__=="__main__":
    matrix=[]

    for i in range(8):
        row=list(map(int,input().split()))
        matrix.append(row)

    # for row in matrix:
    #     print(' '.join(map(str,row)))

    idxs_rook=[]
    idxs_rook=findrook(matrix)
    #print(idxs_rook)
    #[[3, 6], [7, 7]]

    step3=step3(idxs_rook, matrix)
    #print(step3)
    # [-1, -1] or [3,2]

    step4(step3,matrix)



