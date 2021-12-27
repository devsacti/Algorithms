# 최단 거리 dijkstra
from collections import defaultdict
import heapq
import sys
input=sys.stdin.readline

INF = int(1e9)

def dijkstra(graph,s,shortests):
    shortests[s]=0
    pq=[]
    # distance를 기준으로 제일 거리가 가까운 곳을 추출해서 우선순위 큐에 넣는 것을 이해
    heapq.heappush(pq,(0,s))
    
    while(pq):
        # candidate of shortests
        cand, now = heapq.heappop(pq)

        # 이미 다른 경로로 현재 노드에 접근했었는데 그 코스트가 더 싼 경우
        if(cand>shortests[now]): continue
        # 
        for adj in graph[now]:
            # graph[now] means adj list, and adj[1] means cost
            cost = cand + adj[0]
            # adj[0] means index of adj like 0~n
            if(cost<shortests[adj[1]]):
                shortests[adj[1]] = cost
                heapq.heappush(pq, (cost,adj[1]))

if __name__=="__main__":
    n,m = map(int,input().split())
    graph={}
    shortests=[INF]*(n)

    for _ in range(m):
        v, adj = map(int,input().split())
        cost=1

        graph[v].append((cost,adj))
        graph[adj].append((cost,v))

    s,e = map(int,input().split())
    # print(*graph, sep='\n')

    dijkstra(graph,s,shortests)
    # print(distance)
    print(shortests[e])
    print(shortests)