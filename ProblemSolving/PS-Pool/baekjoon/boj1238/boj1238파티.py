'''
ps1 comprehension about problem
ps1.1. analysis
ps1.2. drawing pattern, exception

ps2. applying computer algorithms to comprehension
ps2.1. utilizations
ps2.2. integrations

ps3. Impl
# for문의 k와 인풋 k 가 중첩!
'''
from collections import defaultdict
import heapq

def dijstra(graph,s,shortests):
    shortests[s]=0
    pq=[]
    heapq.heappush(pq,(0,s))

    while pq:
        cand_shortest,now=heapq.heappop(pq)

        if(cand_shortest>shortests[now]):
            continue

        for adj in graph[now]:
            interval, next=adj
            cand_shortest=shortests[now]+interval

            if(cand_shortest<shortests[next]):
                shortests[next]=cand_shortest
                heapq.heappush(pq,(cand_shortest,next))
    
    return shortests

if __name__=="__main__":
    n,m,k=map(int,input().split())

    graph=defaultdict(list)

    inf=int(1e20)

    for _ in range(m):
        v1,v2,interval = map(int, input().split())

        graph[v1].append((interval,v2))

    keys=sorted(list(graph))
    # for key in keys:
    #     print(key,' ',graph[key])

    total_distance=0

    end=k

    for start in range(1,n+1):
        if(start==k):continue

        # print(start,end)
        # start to end
        shortests=[inf for _ in range(n+1)]
        shortests=dijstra(graph,start,shortests)
        total_distance+=shortests[end]
        # print(shortests)

        # end to start
        shortests=[inf for _ in range(n+1)]
        shortests=dijstra(graph,end,shortests)
        total_distance+=shortests[start]
        # print(shortests)
    print(total_distance)
