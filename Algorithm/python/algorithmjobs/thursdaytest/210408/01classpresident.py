import sys

if __name__=="__main__":

    n=int(sys.stdin.readline().strip())
    set_acquaintance=[set() for _ in range(n)]

    matrix=[]
    for _ in range(n):
        row=list(map(int,sys.stdin.readline().split()))
        matrix.append(row)

    transposed_matrix=list(zip(*matrix))

    for idx_student in range(n):
        for idx_class in range(5):

            std_classnum=matrix[idx_student][idx_class]

            related_classrecord=transposed_matrix[idx_class]

            for idx_std,experi_class in enumerate(related_classrecord):
                if(std_classnum==experi_class):
                    set_acquaintance[idx_student].add(idx_std)
    
    # print(set_acquaintance)

    max_cnt_friend=-100
    idx_president=-1
    for idx_s,case in enumerate(set_acquaintance):
        if(len(case)>max_cnt_friend):
            idx_president=idx_s
            max_cnt_friend=len(case)
    
    print(idx_president+1)
