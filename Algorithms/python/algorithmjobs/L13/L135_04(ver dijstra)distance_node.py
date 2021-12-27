import sys
from collections import deque
import heapq



def bfs_distance(start, target):
    global Tree, visited
    # start, target ; INDEX OF COMPUTER

    deque=deque()
    deque.append(start)

    while(deque):
        # 참고로 인접노드 방문 순서는 초기화 절차 그대로를 거쳐서 오름차순이됨
        curNode=deque.popleft()

        if(curNode not in visited):
            # visit ck of cur node, first is start node
            visited.append(curNode)

            if(curNode==start):
                stacked_distance=0
                dist[curNode]=stacked_distance
                exNode=curNode
            else:
                dist[curNode]=dist[exNode]+1

            # get the adjacent node of start
            deque.extend(Tree[curNode])

            # 부득이하게 미래 값 활용, 단 인접노드 없으면 가중치 제로
            if(len(Tree[curNode]) ==0 ):
                pass
            else:
                stacked_distance+=1


if __name__=="__main__":
    # Tree of Graph
    Tree=[list() for _ in range(1000)]
    # visitedTree=[False for _ in range(1000)]
    visited=list()

    n,X,Y = map(int, sys.stdin.readline().split())

    # bidirectional for bfs
    for _ in range(n-1):
        idx_node, child = map(int, sys.stdin.readline().split())
        Tree[idx_node].append(child)

        child, idx_node = idx_node, child
        Tree[idx_node].append(child)

    for idx_node,child in enumerate(Tree):
        if(len(child)>0):
            print(idx_node, child)


    