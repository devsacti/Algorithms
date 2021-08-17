# summary of ps

# ps
## Accurate comprehension
# 마지막 지점의 번호는 항상 1이다. 즉, 루트노드의 번호는 1이다
# 이런 조건이 없었다면, reversed_tree를 dfs로 해서 부모노드가 없을때까지 탐색

# 한번의 순회를 통해 inner와 leaf를 도출하고, 첫방문노드에 1을 기준으로 부모와 자식 노드들의 할당비를 
# 구할 수 없을까 고민했지만, 유리수의 문제가 너무 컸다. 즉, leaf에 할당비를 1로 두고 해야 오차가 없다.

## utils-integ algo
# root, inner, leaf로 노드 구분 - bfs

# leaf를 기준으로, 역트리를 활용해서, 노드별 할당비 도출 및 할당 - dfs

## 당연히 bfs 대신 dfs, dfs 대신 bfs도 가능, 추후 연습


## implement
# 트리에서 간선의 갯수는 노드 수 -1
# 일반적인 dfs 순회의 경우 visited가 필요한데, 여기선 중복방문이라 변형필요
# visited 대신 부모노드 존재여부로 전환하는데, for의 if특성과 defaultdict로 해결
# tree가 아닌 그래프였고, 나아가, root부터 인풋하지 않았기에 재구조화 필요
from collections import defaultdict
from collections import deque

# visited 대신 중복방문 허용 dfs
def dfs(tree,v,weights):
  
  if(weights[v]==0):
    weights[v]=1
  else:
    weights[v]+=1
  

  for adj in tree[v]:
    dfs(tree,adj,weights)
  

def bfs(tree,s,visited,inners,leafs):
  visited[s]=1
  q=deque()
  q.append(s)
  
  while q:
    now=q.popleft()
    
    # root is given as 1
    # inner vs leaf
    if(now != 1):
      if(len(tree[now])==0):
        leafs.append(now)
      else:
        inners.append(now)
        
    for adj in tree[now]:
      if(visited[adj]==0):
        visited[adj]=1
        q.append(adj)
        
  
  return inners,leafs

if __name__=="__main__":
  n,b=map(int,input().split())
  
  tree=defaultdict(list)
  reversed_tree=defaultdict(list)
  
  for _ in range(n-1):
    parent, child = map(int,input().split())
    
    tree[parent].append(child)
    
    reversed_tree[child].append(parent)
  print(tree)
  print(reversed_tree)
  
  visited=['*']+[0 for _ in range(n)]
  inner_nodes=[]
  leaf_nodes=[]
  
  inner_nodes,leaf_nodes=bfs(tree,1,visited,inner_nodes,leaf_nodes)
  
  print(inner_nodes)
  print(leaf_nodes)
  
  weights=[0]+[0 for _ in range(n)]
  
  # 도출된 leaf들마다 dfs
  for leaf in leaf_nodes:
    dfs(reversed_tree,leaf,weights)
    
  # print(weights)
  
  div=sum(weights)
  
  # if(b%div==0):
  #   print(b//div)
  # else:
  #   print(-1)