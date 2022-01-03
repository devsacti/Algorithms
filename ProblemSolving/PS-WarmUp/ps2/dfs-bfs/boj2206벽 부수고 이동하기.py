'''
link : https://www.acmicpc.net/problem/2206

ps1. comprehension of problem
ps1.1. analysis

from (1,1) to (N,M) 최단거리; 1 base indexing 
1 하나 삭제 가능
상하좌우로만 이동

ps1.2. drawing pattern, exception

bruteforce 방식으로 벽마다 사라졌을때의 최단거리를 구한다.

ps2. applying computer algorithms to comprehension
ps2.1. utilizations of computer algorithms
ps2.2. integrations

ps3. Impl
'''

if __name__=="__main__":
    n,m = map(int, input().split())

    matrix_maze=[list(map(int,list(input()))) for _ in range(n)]

    print(*matrix_maze,sep='\n')