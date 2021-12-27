import sys

# 기본 dfs는 방문 유무로 다음 노드 선택
# 여기서는 유한한 노드를 리밋으로 두고, 같은 컬러를 기준으로 순회
# 같은 컬러이다 또는 컬러가 없다, 다르다

# 근데 애초에 visited가 순회 중 이전에 대한 걸 피하는 역할인데,
# 하다보니까 이걸 빼니 color만으로 작동안되는 문제 발생.
# color만으로도 되는 방법이 있는것 같지만 나는 기본에 충실한다.

# 방문 유무 T F
# 흑백 T F

# 참고 코드에서도 방문유무를 없앤게 아니라, 컬러 없음 이란 의미의 0 을 활용중이었다.
# 즉, 방문 유무는 체크중이었다. 좀더 압축적이었을뿐

# 그리고 방문유무 체크보단 인접 색깔 체크가 우선이 되야 문제를 해결할수 있기에
# 나의 기본에 충실한 방문유무 체크 후 action은 수정필요, 사실 방문유무 체크도 action이지

def dfs_color( cur_node, color):
    global graph,samecolored
    global visited,token_possible

    # print(cur_node, color)
    # print(list(enumerate(samecolored)))

    visited[cur_node]=True
    samecolored[cur_node] = color
    # print('#',list(enumerate(samecolored)))

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

    graph=[[] for _ in range(N)]
    visited=[False for _ in range(N)]
    samecolored=[None for _ in range(N)]

    token_possible=True

    for _ in range(M):
        #bidirectioanl
        idx_node,child=map(int, sys.stdin.readline().split())
        graph[idx_node].append(child)

        child,idx_node = idx_node,child
        graph[idx_node].append(child)

    # print(graph)
    
    # color는 없음 흑 백, NULL 0 1, None False True
    color=True
    dfs_color(0,color)
    # print(samecolored)

    if(token_possible):
        print("YES")
    else:
        print("NO")
