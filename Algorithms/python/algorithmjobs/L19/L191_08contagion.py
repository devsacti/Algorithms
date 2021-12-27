# 전염병
# bfs 유형
# 오전 6:13 2021-04-19

# 이게 왜 bfs인가 했는데, 1개의 노드로 인해 전염병 로직 상 인접하다고 할수있는 노드 2개가 발생
# 그리고 그 노드 2개는 각자 또다시 밀접한 노드 2개씩 발생
# 어떻게 보면 갈래의 갯수가 일정한 재귀구조는 큐로도 이해가능함을 알게됨

# 의미적으로는 특정 로직에 의해 인접하다고 판단되는 노드들을 바이러스가 방문해 나가는것
import sys
from collections import deque

def bfs_virus(v):
    global willbevisited,cnt_visitedbyVirus

    q=deque()
    willbevisited[v]=1
    q.append(v)

    while(q):
        cnt_visitedbyVirus+=1

        curV = q.popleft()

        adjs=[]
        if(curV*2<=N):
            adjV1= curV*2
            adjs.append(adjV1)

        if(curV//3>0):
            adjV2 = curV//3
            adjs.append(adjV2)

        for adj in adjs:
            if(willbevisited[adj]==0):
                willbevisited[adj]=1
                q.append(adj)

if __name__=="__main__":
    N,K = map(int, sys.stdin.readline().split())

    global willbevisited, cnt_visitedbyVirus
    # NOT USING 0 INDEX
    willbevisited=[0]*(N+1)
    cnt_visitedbyVirus=0

    bfs_virus(K)

    print(N-cnt_visitedbyVirus)