import sys
import itertools

if __name__=="__main__":
    n, m = map(int, sys.stdin.readline().split())

    # tmp_samplespace='1'*n
    # # print(tmp_samplespace)
    # tmp_result=itertools.combinations(n, m)

    # print(len(list(tmp_result)))

    start_row=[1,1]
    pascal_matrix=[]
    pascal_matrix.append(start_row)
    # print(pascal_matrix)

    # r,c : INDEX OF COMPUTER
    for r in range(n-1):
        row=[1]

        for c in range(len(pascal_matrix[r])-1):
            row.append(pascal_matrix[r][c]+pascal_matrix[r][c+1])

        row.append(1)

        pascal_matrix.append(row)

    # print(*pascal_matrix,sep='\n')
    print(pascal_matrix[n-1][m])