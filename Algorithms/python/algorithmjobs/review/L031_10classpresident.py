import sys

# for문에서 갱신해야할 max_friend 놓치고
# computer idx -> real idx 전환 빼먹고
# 5반까지는 고정이고, 학생수는 1000까지라, n*5가 들어올수있는데
# for을 주어진 예시만 보고 n*n으로 함. 어큐러시

# 집합의 갯수는 len으로 구해야하는데, 나도모르게 그냥 sum함....
# 안익숙함의 문제

if __name__=="__main__":
    n=int(sys.stdin.readline().strip())

    matrix=[]
    for _ in range(n):
        row=list(map(int, sys.stdin.readline().split()))
        matrix.append(row)

    transposed_matrix=list(zip(*matrix))

    # print(*transposed_matrix,sep='\n')

    set_matrix=[set() for _ in range(n)]
    # print(set_matrix)

    for idx_student in range(n):
        for idx_class in range(5):
            # 가령, 4번 학생(현재 for내에선 이건 상수)
            # 1학년일때 반번호,2학년일때 반번호 등등 을 가진다
            std_classnum=matrix[idx_student][idx_class]
            # print('#current std class', (idx_student+1,idx_class+1),std_classnum)

            # Trans 된 행렬특징상, idx_class가 주어지면 그 학년 학생들이
            # 각자 몇반인지 알 수 있다. 가령, idx_class가 3(4반)이면
            # (7, 6, 4, 6, 2)이고 자료 특성상, idx_student는 enum을 통해
            # 도출가능
            # print(transposed_matrix[idx_class])
            for idx_s,idx_n in enumerate(transposed_matrix[idx_class]):
                # print('std and experi', std_classnum,idx_s,idx_n)
                if(std_classnum == idx_n):
                    # print(type(set_matrix[idx_student]))
                    set_matrix[idx_student].add(idx_s)
    # print(set_matrix)
    
    max_friend=-100
    for idx_student,unit in enumerate(set_matrix):
        # print(max_friend)s
        if(len(unit)>max_friend):
            # print(idx_student,unit)
            idx_classpresident=idx_student
            max_friend=len(unit)
        else:
            #아는 친구 수가 같은 경우, 갱신 안함으로서 무시
            continue
    # print(set_matrix[idx_classpresident])
    print(idx_classpresident+1)
