# refers

# summary

# PS
## Accurate comprehension about problem
## 트리의 구조에 집중해서 부모노드, 자식노드 그리고 부모 중 루트와 이너를 찾는것도 있지만
## dfs라는 순회를 통해서 노드를 분류하고 정보를 탐색도가능

## Utils and Integration of Algorithms

## Implementation
from collections import defaultdict

# graph includes tree
def dfs(graph,v,visited):
    pass

if __name__=="__main__":
    n,b = map(int,input().split())

    tree = defaultdict(list)
    reversed_tree = defaultdict(list)

    for _ in range(n):
        parent, child = map(int,input().split())

        tree[parent].append(child)

        reversed_tree[child].append(parent)

    all_nodes=[i for i in range(1,n+1)]

    parent_nodes=list(tree)

