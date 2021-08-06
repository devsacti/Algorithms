import sys
from collections import deque
# 노드의 값을 트리상의 인덱스로 쓰는 방식이 위에서 아래도 참조해나갈때는 유의미한데,
# 아래서 위로 갈때는 무의미한듯, 굳이 하자면, 6의 부모를 알고 싶으면
# Tree에서 인덱스가 6미만 노드들 모두를 방문해서 체크는 할 수 있음.

# 아니면 힙형태는 자식수가 불규칙해서 무의미

# 트리를 뒤집으면 참조하기 쉬울듯함, 역함수를 만들기 힘든 트리이니,
# 애당초 역함수가 기본함수인 형태로 트리를 구현, 루트가 맨 마지막 자식이 되는 형태

class Node:
    # 아래와 같은 방식은, 개별 노드들이 같은 childs를 참조하는 문제 발생
    # childs=[]

    # def __init__(self):
    #     self.parent=

    # parent is only one
    parent=-1

if __name__=="__main__":
    n,X,Y =map(int,sys.stdin.readline().split())
    reverse_Tree=[None]*1005
    idx_parent_childs=[0,0]

    parents_x=[]
    parents_y=[]

    for _ in range(n-1):
        # idx_node, child = map(int,sys.stdin.readline().split())
        # reverse tree에 맞춰서 전환
        parent, idx_node = map(int,sys.stdin.readline().split())

        if reverse_Tree[idx_node]==None:
            node=Node()
            node.parent=parent
            reverse_Tree[idx_node]=node
        else:
            reverse_Tree[idx_node].parent=parent

        # 딱히 효과도 없고, 접근방식도 다소 복잡하게 해서 주석
        # if (idx_node == X):
        #     parents_x.append(parent)
        # if (idx_node == Y):
        #     parents_y.append(parent)
    
    # print('---')
    # for idx,node in enumerate(reverse_Tree):
    #     if(node != None) : print(idx,node.parent)
    # print('---')

    # 내 의도와 달리, 한번에 parent를 2칸 씩 체킹하는 문제 발생
    while(reverse_Tree[X] != None):
        # print('init X', X)
        parent_x=reverse_Tree[X].parent
        # print('parent x ',parent_x)

        parents_x.append(parent_x)
        # print('update list', parents_x)

        # print('again parent x ',parent_x)

        X=parent_x
        # 아래와같이하면 부모의부모를 다음 시작으로 설정,
        # 이렇게 2칸씩 이동하니까 while조건도 잘 안돌고
        # X=reverse_Tree[parent_x].parent

        #한편, 맨 위 루트는 다른 자식노드의 하위 값으로만 존재하지
        # None인 것을 놓침

    # print(parents_x)

    while(reverse_Tree[Y] != None):
        # print('init X', X)
        parent_y=reverse_Tree[Y].parent
        # print('parent x ',parent_x)

        parents_y.append(parent_y)
        # print('update list', parents_x)

        # print('again parent x ',parent_x)

        Y=parent_y
        # 아래와같이하면 부모의부모를 다음 시작으로 설정
        # X=reverse_Tree[parent_x].parent
    
    # print(parents_y)

    # 일단 파이썬의 강점을 써보자, 다행히 시간안에는 돌아가는데,
    # 공통인 건 잡아내지만 정확히 최초의 조상을 잡을라면 별도의 절차 필요
    # set_xparents = set(parents_x)
    # set_yparents = set(parents_y)

    # commons=set_xparents and set_yparents
    # # print(commons)
    # print(max(list(commons)))

    # 처음으로 2번 체크되는 값을 구하자
    checklist=[0]*1005
    dq_xparents=deque(parents_x)
    dq_yparents=deque(parents_y)

    while(1):
        if(len(dq_xparents)!=0) : 
            xparent=dq_xparents.popleft()
            checklist[xparent]+=1
        if(checklist[xparent]==2):
            first_common=xparent
            break

        if(len(dq_yparents)!=0) : 
            yparent=dq_yparents.popleft()
            checklist[yparent]+=1

        if(checklist[yparent]==2):
            first_common=yparent
            break

    print(first_common)