import sys

# (1), start one
# (1)+(6), start one and six apex
# (1)+(6)+(6+0), start one and six apex and between six apex 
# (1)+(6)+(6+6), start one and six apex and (between six apex)*2 
# (1)+(6)+(6+6)+(6+0+0), start one and six apex and (between six apex)*2 
#
# 논리 오류, 갯수 증가 패턴을 '잘못 묶음'->수정

if __name__=="__main__":
    N=int(sys.stdin.readline().strip())

    sum_rooms=1
    #init level is 1
    upperlimit_equal=[]
    upperlimit_equal.append(sum_rooms)

    # level 1 to 2 to 3 to 3 ...
    # weight 6*1 to 6*2 to 6*3 ... 
    incre_weigth_perlevel=1
    while(upperlimit_equal[-1]<N):
        subsum=6*incre_weigth_perlevel
        incre_weigth_perlevel+=1
        sum_rooms+=subsum
        upperlimit_equal.append(sum_rooms)

    # print(upperlimit_equal)
    print(len(upperlimit_equal))