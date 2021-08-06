import sys
from collections import deque

# 혹시 노드 생성될때마다 특징을 통해서 높이 도출가능한가 했는되, 왼온반복시 안되고
# 정석적으론 level order? 일단 이거 해보자
# level order는 층위 개념이 없구나...

# 해설보니까 점화식 접근
# ; height = max( hegiht of left subtree, height  of left subtree) +1

# 20점...정말 거의 포기한 영역에 대해서 내 스스로 만든 코드가 많지는 않아도
# 유효하다는 건 기쁜것 같다.

def levelodrder(Tree,root):
    q=deque()

    q.append(root)

    traversal=""
    while(len(q) > 0):
        t=q.popleft()

        traversal += str(t) + '-'

        if(Tree[t] == None):
            pass
        else:
            if(len(Tree[t].childs)>0):
                for item in Tree[t].childs:
                    q.append(item)
            else:
                pass

    print(traversal)
# dfs_Tree_trial1
# 재귀구조를 만듦에 있어, Tree에는 처음 트리 말고, sub Tree가 입력되고
# idx_root로 확정한것에는 sub node들의 idx도 들어감에 따라
# 오직 트리의 첫번째 노드에 맞춰진 첫번째 if else는 보다 추상화될 필요 확인
def dfs_Tree_trial1(Tree, idx_root):
    # cuz to input condition, Tree has at least 1 node,
    # but for practice, check the root node
    '''아래 오직 루트에 대한 if else는 재귀구조에서 오류발생, 2번째로 합병되야한다.'''
    if(Tree[idx_root] == None):
        print('Empty Tree')
    else:
        # root node는 존재하고, 이제 root의 자식들을 검정
        # 나의 노드 클래스 구조에 따라서 자식이 없으면 childs가 none이다.
        if(Tree[idx_root].childs == None):
            partial_height=0
            return sub_height
        else:
            childs_queue=Tree[idx_node].childs
            partial_heights=[]
            #자식이 있다면 일단 부분 길이 1 확보하고, 하위에서 전달받은 걸 체증하는 형태로가보자
            partial_height=1
            while(childs_queue):
                ci_sub_node=childs_queue.popleft()
                partial_height+=dfs_Tree(Tree,ci_sub_node)
                
def dfs_Tree_trial2(powersub_Tree, idx_node):
    # print('cur idx node ',idx_node)
    # cuz to input condition, Tree has at least 1 node,
    # but for practice, check the root node
    #-> 재귀구조 안에서 통합적으로 체크하게 구현해야해서 하위 ifelse에 역할 넘김

    # root node는 존재하고, 이제 root의 자식들을 검정
    # 나의 노드 클래스 구조에 따라서 자식이 없으면 childs가 none이다.

    # 양방향 으로 인해 언제나 양쪽 모두 노드는 생성되게 되었다.
    # 관련하여 방문하고 안하고로 구분된다.
    if(visitedTree[idx_node] == 1):
        partial_height=-1
        #여기에 도달하면, 이전의 방문한 노드이고,
        # 순간 역트리가 형성된다고 할때, '현재 노드를 루트로 가지는 하위 하위트리'의 전체높이는 0
        powersub_height=partial_height
        return powersub_height

    else:
        visitedTree[idx_node]=1
        childs_queue=powersub_Tree[idx_node].childs
        partial_heights=[]
        # 노드로서 존재한다 == 자식 변수가 존재한다 cuz to __init__
        # 자식이 있다면, 즉 지금 노드에서 '앞으로 갈곳이 있다면'
        # 아직 이동하기 '전'이지만
        # 확실히 일어날 사건에 대응하여 높이 1 확보하고,
        # 하위 노드에 1을 빌려줘서 가중치를 더하고 돌려받는다고 생각하면서
        # 큐를 돌려보자

        # 근데 갱신을 while안에서 해야 하위 노드별로 1씩 빌려주는 꼴이된다.
        while(childs_queue):
            partial_height=1
            # print('before ',partial_heights,partial_height)
            ci_sub_node=childs_queue.popleft()
            # 아래 행에서 드디어 다음 노드의 idx를 받아서 이동하는 것이다
            # 'dfs_Tree에 값을 넣는 것'이 
            # 다음 노드로의 이동, 다음 노드로의 도착, 다음 노드의 현재 노드화
            # print('--now goto next node by function--')
            subresult=dfs_Tree_trial2(powersub_Tree,ci_sub_node)
            # print('val from fuction ', subresult)
            partial_height+=subresult
            # print('mid partial height ',partial_height)
            partial_heights.append(partial_height)
            # print('ongoing ',partial_heights)
        # print('after ',partial_heights,partial_height)
        
        # 자식들의 높이에서 가장 큰 높이가 추후 전체가 될 수 있는 부분
        powersub_height=max(partial_heights)
        # print('best of subtree  which will be get back to upper node ',powersub_height)
        return powersub_height

    # 위와같은 if else를 돈 뒤 partial height는
    # 의도된 대로라면 1로 시작하여 하위트리의 whole height가 +된 상태로
    # 전체의 whole 된다. 그런 점에서 power set에 착안하여 power set 속의 sub으로
    powersub_height=partial_height

    return powersub_height
        
'''양방향으로 길이 생기면서 현재 방식, 미래에 갈곳이 있다 ->+1 은
애당초 접근하면 안되는 부모노드에 대해서 1이 가중되는 일이 발생 중

1. 새로운 방식의 dfs 정의
2. 기존 dfs에서 미래값에 할당된 1에 대응하여 1감소 ->90점
'''
# def dfs_Tree_trial3(powersub_Tree, idx_node):
#     # '현재' 도착한 노드와 그 노드에 대한 방문 체크
#     print('cur idx node ',idx_node)
#     visitedTree[idx_node]=1
#     # 양방향 으로 인해 언제나 양쪽 모두 노드는 생성되게 되었다.
    
#     # '미래'
#     #  주변노드들은 방문한 노드와 그렇지 않은 노드로 구분
#     adjacents_queue=powersub_Tree[idx_node].adjacents

#     while(adjacents_queue):
#         cand_visit=adjacents_queue.popleft()

#         if(visitedTree[cand_visit] == 1):
#             continue
#             #복잡하게 생각할거없이, 다음으로 넘어간다.
#         else:
#             #방문해도 되는 것들만 남음,
#             partial_heights=[]

#         if(visitedTree[cand_visit] == 1):
#             partial_height=0
#             #여기에 도달하면, 이전의 방문한 노드이고,
#             # 순간 역트리가 형성된다고 할때, '현재 노드를 루트로 가지는 하위 하위트리'의 전체높이는 0
#             powersub_height=partial_height
#             return powersub_height

#         else:
#             # 부모로도 길은 뚤린 상황이라 child queue에서 adjacent queue로 변경
#             adjacent_queue=powersub_Tree[idx_node].childs
#             partial_heights=[]
#             # 노드로서 존재한다 == 자식 변수가 존재한다 cuz to __init__
#             # 자식이 있다면, 즉 지금 노드에서 '앞으로 갈곳이 있다면'
#             # 아직 이동하기 '전'이지만
#             # 확실히 일어날 사건에 대응하여 높이 1 확보하고,
#             # 하위 노드에 1을 빌려줘서 가중치를 더하고 돌려받는다고 생각하면서
#             # 큐를 돌려보자

#             # 이미 가본 노드는 

#             # 근데 갱신을 while안에서 해야 하위 노드별로 1씩 빌려주는 꼴이된다.
#             while(childs_queue):
#                 partial_height=1
#                 print('before ',partial_heights,partial_height)
#                 ci_sub_node=childs_queue.popleft()
#                 # 아래 행에서 드디어 다음 노드의 idx를 받아서 이동하는 것이다
#                 # 'dfs_Tree에 값을 넣는 것'이 
#                 # 다음 노드로의 이동, 다음 노드로의 도착, 다음 노드의 현재 노드화
#                 print('--now goto next node by function--')
#                 subresult=dfs_Tree_trial2(powersub_Tree,ci_sub_node)
#                 print('val from fuction ', subresult)
#                 partial_height+=subresult
#                 print('mid partial height ',partial_height)
#                 partial_heights.append(partial_height)
#                 print('ongoing ',partial_heights)
#             print('after ',partial_heights,partial_height)
            
#             # 자식들의 높이에서 가장 큰 높이가 추후 전체가 될 수 있는 부분
#             powersub_height=max(partial_heights)
#             print('best of subtree  which will be get back to upper node ',powersub_height)
#             return powersub_height

#         # 위와같은 if else를 돈 뒤 partial height는
#         # 의도된 대로라면 1로 시작하여 하위트리의 whole height가 +된 상태로
#         # 전체의 whole 된다. 그런 점에서 power set에 착안하여 power set 속의 sub으로
#         powersub_height=partial_height

#         return powersub_height

# 추후 dfs의 연산과정을 위해서 처음에는
# None으로 초기화하고, 노드 생성후 별도로 '들어올값이 있는 상황'에 대응하여
# childs를 데크로  갱신하기로 결정
class Node:
    def __init__(self):
        self.childs=None

# 양방향으로 인해 child보단 adjacent
# class Node:
#     def __init__(self):
#         self.adjacents=None

if __name__=="__main__":
    total_height=0

    Tree=[None]*105
    visitedTree=[None]*105

    n,r = map(int, sys.stdin.readline().split())

    for _ in range(n-1):
        idx_node, val_child = map(int, sys.stdin.readline().split())

        if(Tree[idx_node]==None):
            node=Node()
            node.childs=deque()
            node.childs.append(val_child)
            Tree[idx_node]=node
        else:
            Tree[idx_node].childs.append(val_child)

        # fucking bidirectional
        val_child, idx_node = idx_node, val_child

        if(Tree[idx_node]==None):
            node=Node()
            node.childs=deque()
            node.childs.append(val_child)
            Tree[idx_node]=node
        else:
            Tree[idx_node].childs.append(val_child)


    # print('--')
    # for idx,node in enumerate(Tree):
    #     if(node != None):
    #         print(idx, node.childs)
    # print('--')

    # levelodrder(Tree,r)

    total_height=dfs_Tree_trial2(Tree,r)

    print(total_height)

