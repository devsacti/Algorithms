import sys

# 방문여부를 감염여부로 확장 또는 치환하는 것

# in this case, color means same group
def dfs_basic(cur_node):
    # cur node : NOT INDEX OF COUMPUTER

    global graph, visited
    global cnt_infested
    
    # print(cur_node, color)

    # checking the infested
    if(cur_node==1):pass
    else:cnt_infested+=1

    visited[cur_node]=True
    # print('#',list(enumerate(samecolored,1)))

    # print(graph[cur_node])
    # 기본적인 순회를 위한 dfs
    for adj in graph[cur_node]:
        if(visited[adj]): continue
        else:
            dfs_basic(adj)


if __name__=="__main__":
    # N means cnt of vertex
    N=int(sys.stdin.readline().strip())
    # M means cnt of edges
    M=int(sys.stdin.readline().strip())

    # cuz to input condition, node start from '1'
    # so make the one more with not using 0
    graph=[[] for _ in range(N+1)]
    visited=[False for _ in range(N+1)]
    
    global cnt_infested
    cnt_infested=0

    for _ in range(M):
        #bidirectioanl
        idx_node,child=map(int, sys.stdin.readline().split())
        graph[idx_node].append(child)

        child,idx_node = idx_node,child
        graph[idx_node].append(child)

    print(graph)
    
    # start node is fixed with 1
    dfs_basic(1)

    print(cnt_infested)
