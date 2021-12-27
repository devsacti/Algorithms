import sys
# 인접리스트로 역트리를 만들자.

def findsparent(idx_node, parents):
    global reversed_Tree
    # print('cur idx ', idx_node)

    if(len(reversed_Tree[idx_node]) != 0):
        # list나 deque에서 pop은 원본을 변형한다. 배열로 쓸때는 인덱스로 접근
        parent=reversed_Tree[idx_node][0]
        parents.append(parent)
        # print(parents)
        findsparent(parent,parents)
    else:
        pass
    
    return parents

if __name__=="__main__":
    n,X,Y = map(int, sys.stdin.readline().split())
    MAX=1005
    reversed_Tree=[list() for _ in range(MAX)]

    for _ in range(n-1):
        child, idx_node = map(int, sys.stdin.readline().split())

        reversed_Tree[idx_node].append(child)

    # print('--')
    # for idx,node in enumerate(reversed_Tree):
    #     if len(node) != 0 : print(idx, node)
    # print('--')

    xparents=[]
    xparents=findsparent(X, xparents)

    yparents=[]
    yparents=findsparent(Y, yparents)

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