# summary of ps

# ps
## Accurate comprehension
# 마지막 지점의 번호는 항상 1이다. 즉, 루트노드의 번호는 1이다
# 이런 조건이 없었다면, reversed_tree를 dfs로 해서 부모노드가 없을때까지 탐색

# 두 지점이 서로 연결되어있다는 의미 >> 부모자식이랑 별개의 무방향 간선 정보로서 층위와 무관하게 줘서 별도 처리 필요
## 우선 인풋값 받을 당시엔 무엇이 부모인지 알수없어, 양방향으로 연결하되,
## 1번이 루트라는 조건에 따라 1번부터 살펴보고, 부모로의 방향은 끊으면 된다.

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


# dfs for finding leaf of tree
def is_leaf(tree, v, visited, leafs, weights):
    if (len(tree[v]) == 0):
        leafs.append(v)
        weights[v] = 1

    for adj in tree[v]:
        if (visited[adj] == 0):
            is_leaf(tree, adj, visited, leafs, weights)


# directed edge, so visited don't needed
def dfs(reverse, v, weights):
    for adj in reverse[v]:
        weights[adj] += 1
        dfs(reverse, adj, weights)


# bfs for making tree from graph
def make_tree(graph, s, visited, tree, reversed_tree):
    visited[s] = 1
    q = deque()
    q.append(s)

    while q:
        now = q.popleft()

        # 양방향 그래프라 여기는 안됨
        # tree[now].extend(graph[now])

        for adj in graph[now]:
            if (visited[adj] == 0):
                # 현재 기준 방문안한 애들이 자식임
                tree[now].append(adj)
                visited[adj] = 1
                q.append(adj)
            else:
                reversed_tree[now].append(adj)

    return tree, reversed_tree


if __name__ == "__main__":
    n, b = map(int, input().split())

    graph = defaultdict(list)

    # 간선 정보다 층위와 별개라 v1,v2로 정정
    for _ in range(n - 1):
        v1, v2 = map(int, input().split())
        # 무방향 그래프로 우선 선언
        graph[v1].append(v2)
        graph[v2].append(v1)

    keys = sorted(list(graph))

    # for k in keys:
    #   print(k,':',graph[k])

    tree = defaultdict(list)
    reversed_tree = defaultdict(list)

    visited = ['*'] + [0 for _ in range(n)]

    tree, reversed_tree = make_tree(graph, 1, visited, tree, reversed_tree)

    # print(tree)
    # print(reversed_tree)

    # tree와 reversed_tree의 관계를 이용해서 아래를 찾을 수도 있는데 O(n^2)라 지양
    leaf_nodes = []
    visited = ['*'] + [0 for _ in range(n)]
    weights = [0] + [0 for _ in range(n)]

    is_leaf(tree, 1, visited, leaf_nodes, weights)

    # print(leaf_nodes)
    # print(weights)

    # 도출된 leaf들마다 dfs
    for leaf in leaf_nodes:
        dfs(reversed_tree, leaf, weights)

    # print(weights)

    div = sum(weights)
    # print(div)

    if (b % div == 0):
        print(b // div)
    else:
        print(-1)