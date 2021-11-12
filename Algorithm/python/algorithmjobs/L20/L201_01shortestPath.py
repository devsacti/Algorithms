# 최단 거리 dijkstra
# 오후 5:51 2021-05-14
# core content ; dijkstra = dp, bfs

# dp 적 관점에서 dijstra 이해하기
# distance list를 dp table로 이해한다면,
# 지금 distance list의 해당 인덱스에 들어 있는 값은, '이전까지' 최적해, 즉 최단거리를 충족한다고 볼수있다.

# 이러한 상황에서 현재 방문 목적지_now_에서 다시금 dp table의 값이 최적값인지 체크한다.
# 다만, 단순히 더 빠른 길을 찾았다고 바로 갱신하면 안된다.

# 왜냐하면 현재 방문 목적지, 측 target에는 최초에 접근을 시도한 노드 외에도
# 인접노드들이 존재하므로 이들을 경유했을 때 나오는 최단거리, 최적값을 검증해야한다.

# 정리하자면,
# 목적지에 접근을 시도하는 첫번째 노드를 통해서 목적지의 최단거리를 갱신할 가치가 있는지 점검하고
# 그리고 갱신할 가치가 있다면, 그 인접노드까지 전부 확인해서 진정한 최단거리를 찾는것으로 일단 이해


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