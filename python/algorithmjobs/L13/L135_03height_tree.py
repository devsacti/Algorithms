import sys

def dfs(curNode, dist):
    # start : INDEX Of COMPUTER
    global Tree, visited
    global MAX_dist
    # print('cur node ', curNode, dist, MAX_dist)
    
    # 이전 dist+1은 현재 노드 방문처리 직후,
    visited.append(curNode)
    # powersub으로 정의된 후 최단거리를 갱신, 만약 하위 노드가 없다면
    # 최하단 return에 활용; 더이상 갈곳이 없고, 현재까지 이만큼 달려왔다의 의미
    powersub_dist=dist

    # 기능상 여기도 상관없는데, 점화식의 논리와는 상충, 각 하위 트리의 최대를 갱신하는 형태이므로    
    # if(powersub_dist>MAX_dist):
    #     MAX_dist=powersub_dist

    # 리스트가 비어있으면 아래 for문은 작동하지 않는다.
    # 자동으로 if (하위 노드 유무 판단) 작동
    '''아래 for문은 일종의 if else로 노드 있으면 for작동, 없으면 리턴이다'''
    for node in Tree[curNode]:
        if(node not in visited):
            # 여기서 dist+1은 방문도 하기 전에 1증가가 아니라,
            # 방문 후 1 증가를 위해 준비된 것이지 아직 갱신된 것 아님
            powersub_dist=dfs(node,dist+1)

            # 각기 다른 하위 트리에서 거리를 갱신한 후 그 중 최대값을 찾는 상황
            if(powersub_dist>MAX_dist):
                MAX_dist=powersub_dist

    return powersub_dist

if __name__=="__main__":
    # Tree from graph
    MAX = 1000
    Tree=[list() for _ in range(MAX)]
    visited=[]
    MAX_dist=0

    n,r = map(int, sys.stdin.readline().split())

    for _ in range(n-1):
        # parent , child : INDEX of COMPUTER
        parent, child = map(int, sys.stdin.readline().split())
        Tree[parent].append(child)

        # bidirectional
        child, parent = parent, child
        Tree[parent].append(child)

    # print('--')
    # for idx,node in enumerate(Tree):
    #     if(len(node) != 0):
    #         print(idx, node)
    # print('--')

    init_dist=0
    result=dfs(r,init_dist)

    print(MAX_dist)
    