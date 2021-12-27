import sys

#curNode : INDEX OF COMPUTER
def dfs_height(curNode, curHeight):
    global maxHeight
    # print('#',curNode, curHeight)

    visited[curNode]=True

    # 자식이 없다면, 지금까지의 높이가 현재 갈래에선 최대
    # 자식이 있다면, 더 알아봐야함
    # 따라서, 아래

    # 현재까지 높이와 최대 비교; powersub의 특징
    if(curHeight>maxHeight):
        maxHeight=curHeight
    
    # 자동으로 인접노드가 있을때 작동
    for adj in Tree[curNode]:
        if(visited[adj]): continue
        else:
            dfs_height(adj, curHeight+1)


if __name__=="__main__":
    n,r = map(int, sys.stdin.readline().split())

    Tree=[[] for _ in range(n)]
    visited=[False]*n

    global max_height
    maxHeight=0
    curHeight=0

    for _ in range(n-1):
        idx_node, child = map(int, sys.stdin.readline().split())
        Tree[idx_node].append(child)

        child, idx_node = idx_node, child
        Tree[idx_node].append(child)

    print(Tree)
    dfs_height(r,curHeight)
    print(maxHeight)
