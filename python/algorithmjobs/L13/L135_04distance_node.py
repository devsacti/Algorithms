import sys

# class Node:
#     def __init__(self):
#         self.childs=None
# 인접 리스트로 graph 만드는 게 더 편하더라

# 재귀구조의 depth 개념이 구체화되서 distance가 되는듯, 이걸 포괄할 변수명이 있을까

# 전체 노드에 대해서 일반적인 재귀구조 형태로 짰더니, 거리는 도출됬는데, 그 후에도 재귀가 돌음,
# 추가적인 토큰으로 break하기에도 층위구조안에서 잘작동할지 모르겠음,
# 일단 값을 받고 토큰에 따라서 갱신되게 만들어보기로 결정

'''
예제에만 사로잡혀서 못봤는데, 좌우 균일하게 있을때는
루트를 중심으로 각각 거리 구해서 합하면되지만, 아닐때는 bfs형태인듯

해결책 1
일단 앞선 교과와 인풋값 성질(부모자식) 충실해서 공통조상찾기 모듈 끌어다가,
xy의 공통조상 노드 찾고 공통조상을 루트로 각 노드와의 거리를 합한다.
-> reverse 트리와 기본 트리를 둘다 만들어야 한다. 못할건 없지만 복잡한 느낌
-> 기본트리 안만들어도 됨 역트리 에서 거슬러 올라갈때 거리 구하면되니까

해결책 2 (최종선택)
시작노드를 루트로 트리를 변형한다(애당초 양방향 간선으로 만들면). 루트에서 해당노드까지 높이로 거리 출력
-> 주어진 값이 굳이 부모 자식 노드라는 데 오바하는 것 같다

해결책 3 ? bfs와 다익스트라
문제 의도는 질문하되(dfs? bfs? bfs라면 어찌)
bfs 버전은 추후 다익스트라와 결부해서 풀기로 함.

참고,
다익스트라 알고리즘은 '한 점' 또는 이동한 후의 '특정 점'을 기준으로
모든 점까지의 최단 거리를 갱신하면서 모든 점에 대한 최단 거리를 구한다.
https://www.fun-coding.org/Chapter20-shortest-live.html

'''

# 재귀구조 상, 상위의 for문이 남아있기 때문에 한 갈래의 단순히 return만으로
# 변수가 온전히 도착하기 힘듦, 그냥 전체 도는 과정에서 필요값만 챙기는 방식으로 전환
def dfs(curNode,target, dist):
    # start : INDEX Of COMPUTER
    global Tree, visited
    global target_dist

    # print(curNode, target, dist)
    visited.append(curNode)
    powersub_dist=dist

    if(curNode==target):
        target_dist=powersub_dist

    for node in Tree[curNode]:
        if(node not in visited):
            powersub_dist=dfs(node,target,dist+1)
            # 필요없는 최대 거리 갱신은 제외, 그냥 dfs는 돈다.
        
    return powersub_dist

if __name__=="__main__":
    # Tree from graph
    MAX = 1000
    Tree=[list() for _ in range(MAX)]
    visited=[]

    target_dist=0

    n, X, Y = map(int, sys.stdin.readline().split())

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
    init_dist=dfs(X,Y,init_dist)

    print(target_dist)

    