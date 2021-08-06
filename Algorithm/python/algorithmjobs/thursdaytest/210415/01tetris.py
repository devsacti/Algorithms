import sys

if __name__=="__main__":
    C,R = map(int, sys.stdin.readline().split())

    matrix=[]
    for _ in range(R):
        row = list(map(int, sys.stdin.readline().split()))
        matrix.append(row)

    # print(*matrix,sep='\n')

    transposed_matrix=list(map(list,zip(*matrix)))
    # print(*transposed_matrix,sep='\n')

    zeroidx_stack=list()
    cnt_gameover=0
    placeNpoint=[]
    token_gameover=True

    for idx_row,row in enumerate(transposed_matrix):
        preserved_row=row[:]
        # print('#', idx_row,row)

        point_perrow=0
        
        # 행별 0의 idx 수집
        zeroidx_stack=[]
        for idx,val in enumerate(row):
            if(val == 0):
                zeroidx_stack.append(idx)
            else:
                break

        # print(len(zeroidx_stack))
        # 최대 4번 row의 마지막_혹은 최신 추가_인덱스부터 1로 변환
        if(len(zeroidx_stack)<4):
            #gameover case cuz to out of range
            cnt_gameover+=1
            continue
        else:
            # 최대 4번 0에서 1로 전환
            limit_equal=4
            while(limit_equal>0):
                row[zeroidx_stack.pop()]=1
                limit_equal-=1
        # print('##', idx_row,row)
        
        # print('--')
        # print(*transposed_matrix, sep='\n')

        if(cnt_gameover==C):
            token_gameover=False
            break
        
        # 막대기 삽입됬고, 평가해야될 상황
        evaluation_matrix=list(map(list,zip(*transposed_matrix)))
        for row in evaluation_matrix:
            if(sum(row)==C):
                point_perrow+=1

        transposed_matrix[idx_row]=preserved_row

        # 득점이 난 상황만 추가
        if(point_perrow !=0): placeNpoint.append( (idx_row,point_perrow) )

    # print(placeNpoint)
    # 범위 외 게임오버는 아니고, 득점 없는 게임오버
    if(len(placeNpoint)==0):
        token_gameover=False

    if(token_gameover):
        sorted_placeNpoint=sorted(placeNpoint,key=lambda x:x[1])
        bestplace, point = sorted_placeNpoint[-1][0]+1,sorted_placeNpoint[-1][1] 
        print(bestplace, point)
    else:
        print(0, 0)



        
