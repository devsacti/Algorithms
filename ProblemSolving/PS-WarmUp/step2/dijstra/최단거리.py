# summary

## reference

# PS
## comprehension
## problem
## shortest between v and v

## in & out condi
## n,m ; cnt of vertex, edge, int

## print dist from start to end

## utils & Integration of Algorithms

## heapq and idea of dp

## implementation
from collections import defaultdict
import heapq

inf=int(1e10)

def dijstra(graph, s, shortests):
  shortests[s]=0
  pq=[]
  heapq.heappush(pq,(0,s))
  
  while pq:
    candshortest,now=heapq.heappop(pq)
    
    if(candshortest>shortests[now]):continue
  
    for adj in graph[now]:
      interval, next = adj
      cand=shortests[now]+interval
      
      if(cand<shortests[next]):
        shortests[next]=cand
        heapq.heappush(pq,(cand,next))


if __name__=="__main__":
  n,m=map(int,input().split())
  
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
  