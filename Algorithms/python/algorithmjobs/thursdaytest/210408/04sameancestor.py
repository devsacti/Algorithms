import sys
# from collections import deque

# 역트리를 만들자.

class Node:
    def __init__(self):
        self.child=0

MAX=1005

def findsparent(idx_node, parents):
    global Tree

    # print('cur idx ', idx_node)

    # 구조상 해당노드가 None아 아니라면, 역트리 상에서 자식이 있음;
    # 기본트리로 따지면 부모
    if(Tree[idx_node] != None):
        # popleft는 tree를 소거시켜서 안됨
        # parent=Tree[idx_node].childs.popleft()

        # 범용성을 고려해서 자식을 리스트로 선언했는데, 역트리 조건생각하면 
        # 그냥 인트로
        parent=Tree[idx_node].child
        parents.append(parent)
        # print(parents)
        findsparent(parent,parents)
    else:
        pass
    
    return parents

if __name__=="__main__":
    n,X,Y = map(int, sys.stdin.readline().split())

    Tree=[None for _ in range(MAX)]

    for _ in range(n-1):
        child, idx_node = map(int, sys.stdin.readline().split())

        if(Tree[idx_node] == None):
            node=Node()
            node.child=(child)
            Tree[idx_node]=node
        else:
            Tree[idx_node].child=(child)


    # print('--')
    # for idx,node in enumerate(Tree):
    #     if node != None : print(idx, node.child)
    # print('--')

    xparents=[]
    xparents=findsparent(X, xparents)

    yparents=[]
    yparents=findsparent(Y,yparents)

    # print(xparents,yparents)

    dict_parent={std :1 for std in xparents}
    firstcommon=0
    for yparent in yparents:
        if(yparent not in dict_parent.keys()):
            # 애당초 없는 놈은 논외
            pass
        else:
            dict_parent[yparent]+1
            firstcommon=yparent
            break
    
    print(firstcommon)