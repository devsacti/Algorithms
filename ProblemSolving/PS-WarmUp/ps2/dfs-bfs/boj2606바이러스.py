'''
problem link : https://www.acmicpc.net/problem/2606

ps1 comprehension for problem
ps1.1. analysis
ps1.2. drawing pattern

pattern2.
dfs

ps2. applying computer algorithms to problem
ps2.1. utilizations

recursive
!! from recursive to bruteforce 구현과 비교하자면, 우선 현재 방문 노드를 기점으로 분기점들이 생길수있다.
다만, depth와 limit은 여기도 존재하나, 보다 중요한 대상은 그래프와 방문여부이다


ps2.2. integrations

ps3. Impl
'''
from collections import defaultdict

# recursive for Nqueens
def dfs(graph, visited,now):
    visited[now]=1

    for adj in graph[now]:
        if(visited[adj]==0):
            dfs(graph, visited,adj)

if __name__=="__main__":
    n=int(input())
    cnt_edge=int(input())

    graph=defaultdict(list)

    for _ in range(cnt_edge):
        v1,v2 = map(int,input().split())

        graph[v1].append(v2)
        graph[v2].append(v1)

    keys=list(graph)

    # for key in keys:
    #     print(key,' ',graph[key])
    
    visited=[0]+[0 for _ in range(n)]

    now=1
    dfs(graph, visited,now)
    # print(visited)

    print(sum(visited)-1)