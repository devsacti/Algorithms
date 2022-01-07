'''
ps1. comprehension
ps1.1. analysis
ps1.2. drawing pattern, exceptions

개인적으로 플로이드는 최단거리를 계산하기 시간복잡도가 너무 큰 그래프를 보고,
차라리 노드간의 직전 최단거리를 그어버리면 어떨까라는 생각을 했지 않을까한다.

하지만, 주어진 그래프를 왜곡할수는 없을 것이고, 그래서 생각해낸것이 '1점을 경유'한다는 것으로 생각된다.
우선 이것만으로도, 1점을 경우해서 접근 가능한 이웃 노드들의 최단거리는 도출가능해지나,

노드 간 겨우 1~2개의 간선만 존재하는 거미줄같은 그래프나 트리에서,
즉 한 노드에서 다른 노드로 최단거리로 가기위해선 2개이상의 수많은 노드들을 복잡하게 지나야하는 그래프에서

이것이 어떻게 작동가능한지 개인적으로 궁금했는데,
우선 이산적으로 간선이 1개에서 최대 2개인 복잡한 그래프는 잘 펼치고 정리하면 1줄로 연결된 트리에 불과하고,

1점을 경유해서 최단거리를 도출하는 접근은
가상으로 격리된 두 개의 노드를 연결하는 상상의 최단 거리 직선을 연결하는 행위로 이해할 수 있고,
이는 다른 노드 간 가상의 최단거리 직선과 독립적으로,
삼각형의 사이클을 만들어가는 것으로 이해가능하다.

그리고 이렇게 삼각형의 사이클을 만들다 보면 결국 모든 다각형은 3각형으로 분할가능하므로,
연결된 노드들 간에는 최단거리를 도출가능해지지 않나라고 이해해봤다.


ps2. applying computer algorithms to comprehension
ps2.1. utilizing and modularizing
ps2.2. integration

ps3.Impl
'''
from collections import defaultdict
from heapq import *

def dijstra(graph, s, shortests):
  shortests[s]=0
  pq=[]
  heappush(pq,(0,s))
  
  while pq:
      # 이전 탐색을 통해 도출한 현재 지점까지의 최단거리 후보와 현재 노드
      cand_shortest,now=heappop(pq)
      
      # 문제는 최초의 노드_v0_에서 인접노드들_가령, v1,v2_로 접근할때, 인접노드들 간에 연결 되어있을 수 있다는 것이다.
      # 이 때 최초 노드에서 업데이트한 최단거리_v0 에서 v1_가 v2에서 v1으로 접근할때 최단거리보다 작다면, 최단거리로서 가치가 없고
      # 이를 제대로 예외처리하지 않는다면, 추후 최단거리 산출에서 오차가 생기므로 이렇게 스킵한다.
      if(cand_shortest>shortests[now]):continue
    
      for adj in graph[now]:
        interval, next = adj
        # 지금까지 온 거리 + 다음 인접 노드까지의 거리로 최소 후보값 정의
        cand_shortest=shortests[now]+interval
        
        if(cand_shortest<shortests[next]):
            # if문 안에 들어온 순간 cand_shortest shortest
            shortests[next]=cand_shortest
            heappush(pq,(cand_shortest,next))


if __name__=="__main__":
  n,m=map(int,input().split())
  
  inf=int(1e10)  
  
  graph=defaultdict(list)
  
  for _ in range(m):
    v1, v2 = map(int, input().split())
    
    # (interval between start and destination, dest vertex)
    graph[v1].append((1,v2))
    graph[v2].append((1,v1))
  
  s,e =map(int,input().split())
  
  # for k in sorted(list(graph)): 
  #   print(k,graph[k])
    
  shortests=[inf for _ in range(n)]
  
  dijstra(graph,s,shortests)
  
  print(shortests[e])
  