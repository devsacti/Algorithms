import sys
input = sys.stdin.readline
import numpy as np

# 노드의 수
# 간선의 수
# 서로 연결된 노드와 노드 번호
# 서로 연결된 노드와 노드 번호
# 서로 연결된 노드와 노드 번호


if __name__=="__main__":
    n=int(input().strip())
    matrix=[[0]*n for _ in range(n)]
    # print(*matrix,sep='\n')

    npMatrix=np.array(matrix)
    print(npMatrix)

    m=int(input().strip())
    for _ in range(m):
        r,c = map(int,input().split())

        idxR, idxC = r-1 , c-1

        npMatrix[idxR][idxC]=1
        npMatrix[idxC][idxR]=1

    print(npMatrix)

    result=npMatrix
    # 8 of power means 1 + 7, namely multiple 7times
    for _ in range(8-1):
        result=np.dot(result,npMatrix)
        print(result)
        print('--')

    print(result.sum())