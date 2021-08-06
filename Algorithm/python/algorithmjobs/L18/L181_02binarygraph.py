import sys

# 일단 coloring 로직으로 같은 집단끼리 구별가능
# 기본적인것은 coloring 과정을 별개로 시행하고, 별개의 과정으로 같은 색깔들끼리의 간선 유무 체크
# 과정 중 해결 방법으론 앞썬 색깔을 집단분류로 의미를 치환하고
# 인접 노드 중에 같은 집단이 있을때 break하면 코드 그대로 활용가능

# in this case, color means same group
def dfs_color( cur_node, color):
    # cur node : NOT INDEX OF COUMPUTER

    global graph,samecolored
    global visited,token_possible
    
    # print(cur_node, color)
    # print(list(enumerate(samecolored)))

    visited[cur_node]=True
    samecolored[cur_node] = color
    # print('#',list(enumerate(samecolored,1)))

    # print(graph[cur_node])
    # 우선 인접노드 색깔 체크, 방문유무와 별개
    for adj in graph[cur_node]:
        if(samecolored[adj]==color):
            token_possible=False
            break
    # 기본적인 순회를 위한 dfs
    for adj in graph[cur_node]:
        # color is None(default) or different with cur color
        if(visited[adj]): continue
        else:
            dfs_color(adj,not color)


if __name__=="__main__":
    N,M=map(int, sys.stdin.readline().split())

    # cuz to input condition, node start from '1'
    # so make the one more with not using 0
    graph=[[] for _ in range(N+1)]
    visited=[False for _ in range(N+1)]
    samecolored=[None for _ in range(N+1)]

    token_possible=True

    for _ in range(M):
        #bidirectioanl
        idx_node,child=map(int, sys.stdin.readline().split())
        graph[idx_node].append(child)

        child,idx_node = idx_node,child
        graph[idx_node].append(child)

    # print(graph)
    
    # color는 없음 흑 백, NULL 0 1, None False True
    # in this case,
    #  None means no group, False means 0 group, True means 1 group
    # 
    color=True
    # start node : NOT INDEX OF COMPUTER
    dfs_color(1,color)
    # print(samecolored)

    if(token_possible):
        print("YES")
    else:
        print("NO")
