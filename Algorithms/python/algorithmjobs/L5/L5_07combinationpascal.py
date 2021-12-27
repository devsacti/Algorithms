'''
재귀 팩토리알 이랑 콤비네이션 안쓰고 어떻게 구현하지?
아마도 의도는 파스칼 삼각형 레이어 단위로 생성하라는 의도인듯,
nCr=n-1Cr-1+n-1Cr

공식을 바탕인데 재귀 쓰지 말고 1C0, 1C1의 리스트 [1,1]에서부터 파생시키는
라는 의도인듯
'''

if __name__=='__main__':
    n, m = map(int, input().split())

    source=[1,1]
    matrix=[]
    matrix.append(source)

    for i in range(n-1):
        row=[1]

        for j in range(len(matrix[i])-1):
            row.append(matrix[i][j]+matrix[i][j+1])

        row.append(1)
        matrix.append(row)

    print(*matrix,sep='\n')
    print(matrix[n-1][m])