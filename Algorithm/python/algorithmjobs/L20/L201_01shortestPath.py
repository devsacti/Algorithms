# 최단 거리 dijkstra
# 오후 5:51 2021-05-14
# core content ; dijkstra
import sys
import heapq
input=sys.stdin.readline

global graph
global distance

INF = int(1e9)

def dijkstra(start):
    
    pq = [] # priority queue by heap
    distance[start]=0
    # distance를 기준으로 제일 거리가 가까운 곳을 추출해서 우선순위 큐에 넣는 것을 이해
    heapq.heappush(pq,(0,start))
    
    while(pq):
        # dist : 출발지점으로부터의 현대 노드까지의 최단거리 from distance,
        # now : 노드 인덱스
        dist, now = heapq.heappop(pq)
        # 방문되기에 앞서 이미 now에 해당하는 distance이 갱신되는 형태이다.
        # 그리고 while문을 통해 앞으로 방문할 인접노드들의 cost처리과정이다
        print('cur ',dist,now)
        # 이미 다른 경로로 현재 노드에 접근했었는데 그 코스트가 더 싼 경우
        if(distance[now]<dist): continue
        # 
        for adj in graph[now]:
            # graph[now] means adj list, and adj[1] means cost
            cost = dist + adj[1]
            # adj[0] means index of adj like 0~n
            if(cost<distance[adj[0]]):
                distance[adj[0]] = cost
                heapq.heappush(pq, (cost,adj[0]))

if __name__=="__main__":
    n,m = map(int,input().split())
    graph=[[] for _ in range(n)]
    distance=[INF]*(n)

    for _ in range(m):
        v, adj = map(int,input().split())
        cost =1

        graph[v].append((adj,cost))
        graph[adj].append((v,cost))

    start,end = map(int,input().split())
    # print(*graph, sep='\n')

    dijkstra(start)
    # print(distance)
    print(distance[end])
    print(distance)