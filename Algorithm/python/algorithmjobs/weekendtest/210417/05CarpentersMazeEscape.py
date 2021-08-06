import sys

# sol 1). 
# brute하게 모든 나무들에 대해서 없애본  상황마다 순회하고
# 베스트를 반환

if __name__=="__main__":
    N,M = map(int, sys.stdin.readline().split())

    matrix=[]
    for _ in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        matrix.append(row)

    # 이상적인 최단거리는 dr, dy가 각각 n-1, m-1로 장애물이 없는 경우 총합 n+m-2
    