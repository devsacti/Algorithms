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
    # distance를 기준으로 제일 거리가 가까운 곳을 기준으로 우선순위 큐에 넣는 것을 이해
    heapq.heappush(pq,(0,start))
    
    while(pq):
        # dist : '출발지점'으로부터의 현대 노드까지의 최단거리 from distance,
        # now : 현재 방문 노드 인덱스
        dist, now = heapq.heappop(pq)
        # 방문되기에 앞서 이미 now에 해당하는 distance이 갱신되는 형태이다.
        # 그리고 while문을 통해 앞으로 방문할 인접노드들의 cost처리과정이다

        # 이미 다른 경로로 현재 노드에 접근했었는데 그 코스트가 더 싼 경우
        # 참고로 dist는 이전에 dist+adj[1]_cost_로 정의됬던 값으로 결국 동일한 층위의 cost끼리의 비교이다. 
        if(distance[now]<dist): continue
        # 이 아래에서는 distance[now]>=dist 로서
        # 최단거리 후보로서 자격을 가지고 방문'할' 주변 노드를 pq에 넣는것
        for adj in graph[now]:
            # graph[now] means adj list, and adj[1] means cost
            cost = dist + adj[1]
            # adj[0] means index of adj like 0~n
            if(cost<distance[adj[0]]):
                distance[adj[0]] = cost  # '다음 방문 예정 노드의' 최단거리 갱신
                heapq.heappush(pq, (cost,adj[0]))

if __name__=="__main__":
    n,m = map(int,input().split())
    # 1 based indexinng
    graph=[[] for _ in range(n+1)]
    distance=[INF]*(n+1)

    for _ in range(m):
        v, adj, cost = map(int,input().split())

        graph[v].append((adj,cost))
        graph[adj].append((v,cost))

    start,end = map(int,input().split())
    # print(*graph, sep='\n')

    dijkstra(start)
    # print(distance)
    mid=distance[end]

    distance=[INF]*(n+1)
    dijkstra(1)
    cand1part1=distance[start]

    distance=[INF]*(n+1)
    dijkstra(1)
    cand2part1=distance[end]

    part1=min(cand1part1,cand2part1)
    if(part1==cand1part1):
        distance=[INF]*(n+1)
        dijkstra(end)
        part2=distance[n]
    else:
        distance=[INF]*(n+1)
        dijkstra(start)
        part2=distance[n]
    
    print(part1+mid+part2)