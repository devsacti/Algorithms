import sys

# 일단 파이썬의 강점으로 transpose해서 생각하기 편하게 만들고,
# 행별로 1이 나오기 전까지 0의 갯수 세고
# 그만큼에서 최대 4까지 1 집어넣고
# 다시 transpose해서 행별로 전체가 1인 것 구하고

# 처음 55점-> 문제 조건에 따라 게임오버 시  0 0 출력조건을 충족안하고, 기본로직에 맡김
# 두번째 91 점 -> 게임 오버 안에서도 막대기 맵밖에 삐져나오는 상황 인식안함
# 결국 다 해결은 할텐데, accuracy 어렵다.

def getpoint(inserted_matrix):
    global C
    point=0

    for row in inserted_matrix:
        if(sum(row)==C):
            point+=1

    return point

if __name__=="__main__":
    global C,R
    C,R = map(int, sys.stdin.readline().split())

    matrix=[]
    for _ in range(R):
        row=list(map(int, sys.stdin.readline().split()))
        matrix.append(row)

    # print(*matrix,sep='\n')
    # print('--')

    # 세로 가로 C*R
    transposed_matrix=list(map(list,zip(*matrix)))
    # print(*transposed_matrix,sep='\n')
    # print('--')

    # 행마다, 1*4 막대기가 삽입되는 것이 1 시행
    # 행마다 방문해서 0의 idx저장, 추후 pop으로 1 직전 좌표부터 1로 변환
    # 각 시행별 회득 포인트저장용 리스트, 굳이 규격화하자면 길이는 C 개
    per_row_point=[]
    cnt_gameover=0
    for idx_matrix,t_row in enumerate(transposed_matrix):
        idxs_zero=[]
        preserved_t_row=t_row[:]
        for idx,item in enumerate(t_row):
            if(item==1):
                break
            else:
                idxs_zero.append(idx)

        # 모든 시행마다, 막대기가 맵을 벗어나면 게임 오버판정
        if(len(idxs_zero)<4):
            cnt_gameover+=1
            # print(cnt_gameover)

        # 최대4번 1이 삽입되는 아래 절차가 막대기 삽입
        #길이가 4니까 pop은 최대 4번
        for trial in range(4):
            if(len(idxs_zero)>0):
                critical_idx=idxs_zero.pop()
                t_row[critical_idx]=1
            else:
                break
        #
        # print('inserted at ',t_row)
        # print(*transposed_matrix,sep='\n')

        # 막대기 삽입 후, 생각하기 편하게 trans
        inserted_matrix=list(zip(*transposed_matrix))
        # print(*inserted_matrix,sep='\n')
        # print('--')

        # 획득 포인트 체크
        per_row_point.append(getpoint(inserted_matrix))


        # ! 이전 삽입을 초기화하지 않아서 중복 발생,
        # tmp로 새로 매트릭스 만들까 했는데 처음에 기존 행 따로 빼놓고 행 초기화로 해결

        # 이유는 모르겠고, 아래와같은 방식은 갱신반영이 안되서 패스
        # t_row=preserved_t_row
        # print(t_row)

        # print('getback by ',preserved_t_row)
        transposed_matrix[idx_matrix]=preserved_t_row
        # print(*transposed_matrix,sep='\n')

    # print(per_row_point)

    std=max(per_row_point)

    if(cnt_gameover== C):
        print(0, 0)
    else:
        if(std>0):
            print(per_row_point.index(std)+1 , std)
        else:
            print(0, 0)

