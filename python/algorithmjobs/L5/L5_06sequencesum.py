'''
step1

step2
 if N ==4
 a1+a2, a1+a3, a1+a4
 a2+a3, a2+a4
 a3+a4

 a1 3 ea, a2 1+2, a3 1+1+1, a4 1+1+1 ea
 이 우측상단 파트 합
=> N=k 일때 매트릭스의 전체 합은 2*((k-1)*val_total)

! solving wrong answer
N이 4일때 total은 
    total=matrix[0][1]+matrix[N-2][N-1]
가 맞음, 근데 5이상부터는 다름
'''


if __name__=='__main__':
    N=int(input())

    matrix=[]

    for i in range(N):
        matrix.append(list(map(int,input().split())))

    # print(*matrix,sep='\n')

    sum_matrix=0

    for row in matrix:
        # print(sum_matrix, row, sum(row))
        sum_matrix+=sum(row)
        # print(sum_matrix, row, sum(row))

    # print(sum_matrix)
    #2(N-1)val_total is same with sum_matrix; val_total=a1+a2+a3+...
    val_total=sum_matrix // (2*(N-1))

    # print(val_total)

    # 1행에서 a2~aN을 a1를 공통으로 정리; 3=a1+a2, 6=a1+a3 .. ->a2=3-a1, a3=6-a1
    # and sum(matrix[0])=3+6+7+...=(a1+a2)+(a1+a2)+(a1+a3)+...
    # total fomular에 대입; a1+a2+ ... = val_total -> a1+(3-a1)+... =val_total
    # a1는 우변, 숫자는 좌변
    leftside=sum(matrix[0])-val_total
    #a1는 컴퓨터 로직상 임의로 1로 초기화
    a1=1
    rightside=a1*(N-1-1)

    a1=leftside//(N-2)

    aseq=[]
    aseq.append(a1)

    for element in matrix[0][1:]:
        aseq.append(element-a1)

    # print(aseq)

    for element in aseq:
        print(element, end=' ')