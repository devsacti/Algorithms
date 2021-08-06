import sys

# L13_02 에서는 아래와 같은 트리를 정확히 반대로 구현하는 역트리를 쓴다.
# 멋지니까 기억하자

MAX=100

class Node:
    #val_node is index of Tree
    left=-1
    right=-1

def preorder(index_tree):
    #특정 노드의 인덱스를 받아, 그 하위 서브트리를 출력하는 함수
    if(Tree[index_tree].left ==-1 and Tree[index_tree].right == -1):
        print(index_tree, end=' ')
    else:
        # start at root val=index of tree,
        # then, left val(or sub tree), right val(or sub tree)
        print(index_tree, end=' ')
        if(Tree[index_tree].left !=-1): preorder(Tree[index_tree].left)
        if(Tree[index_tree].right !=-1): preorder(Tree[index_tree].right)

def inorder(index_tree):
    #특정 노드의 인덱스를 받아, 그 하위 서브트리를 출력하는 함수
    if(Tree[index_tree].left ==-1 and Tree[index_tree].right == -1):
        print(index_tree, end=' ')
    else:
        if(Tree[index_tree].left !=-1): inorder(Tree[index_tree].left)
        print(index_tree, end=' ')
        if(Tree[index_tree].right !=-1): inorder(Tree[index_tree].right)

def postorder(index_tree):
    #특정 노드의 인덱스를 받아, 그 하위 서브트리를 출력하는 함수
    if(Tree[index_tree].left ==-1 and Tree[index_tree].right == -1):
        print(index_tree, end=' ')
    else:
        if(Tree[index_tree].left !=-1): postorder(Tree[index_tree].left)
        if(Tree[index_tree].right !=-1): postorder(Tree[index_tree].right)
        print(index_tree, end=' ')


if __name__=="__main__":
    Tree=[None]*MAX
    #Tree[i] means Node[i], Tree=Nodes

    n=int(sys.stdin.readline().strip())

    for _ in range(n):
        a,b,c=map(int,sys.stdin.readline().split())
        #making node (left, right)
        node = Node()
        node.left=b
        node.right=c

        #insert the node at exact index of tree, which means also val_node
        Tree[a]=node
        print(Tree[a].right, end='/')
        print(Tree[a].left)

    # print(Tree[2].left)
    preorder(0);print()
    inorder(0);print()
    postorder(0);print()


