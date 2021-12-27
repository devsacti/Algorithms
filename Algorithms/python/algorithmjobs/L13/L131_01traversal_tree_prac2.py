import sys

# 순회 메소드 실행시키면서 안건데,
# 트리에서 None이란 NULL 보단, 구체적으로 No Node로 이해해야
# 논리의 층위가 맞음, 에러도 정확히 규정하고

# 근데, 이런 전통적인 트리 말고, 거의 배열형식의 트리구조가 있었음...
# 힙메모리처럼 배열 위에 로직을 얹어서 트리로 이해하는...

class Node:
    def __init__(self,value,val_left,val_right):
        self.data=value
        self.left=None if(val_left == -1) else val_left
        self.right=None if(val_right == -1) else val_right

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self):
        self.root=None

    # makeroot는 insert and _insert의 하위호환, 완전트리에서만 작동
    def makeRoot(self, node, left_node, right_node):
        if self.root == None:
            self.root = node
        node.left = left_node
        node.right = right_node

    # insert와 _insert는 한 묶음
    def _insert(self, childNode,cur_node):
        # 일단 나는 bst말고, 데이터값이 같나 다르나만 따지자..
        # 느낌상 cur_node가 parent고 Node가 child같아서 childNode로 변경
        # dont be confusded!! curnode.left is int, 'not yet'
        # but after compare val_int and val of Node come in
        # it will become node

        # 기존 구조를 바탕으로 출력하다보니까 아마도, 맨 아래 자식들이 int라서
        # traversal이 맛이감, 구조들의 층위를 모두 노드로 맞춰야할듯
        if(cur_node.left==childNode.data):
            cur_node.left=childNode
        else:
            cur_node.right=childNode


    # 나는 노드가 들어오는 상황인거같아서 약간 변형_insert의 data->Node_했는데..
    # 일단 해보자
    def insert(self, Node):
        if self.root is None:
            self.root = Node
        else:
            # cuz tree is not empty, first one is complete(makeroot)
            # so, go to the root node and insert
            # dont be confused! self.root was assigned node(Node class)
            self._insert(Node,self.root)

    def preorderTraversal(self, node):
        print(node, end='')
        if(not node.left  == None): self.preorderTraversal(node.left)
        if(not node.right == None): self.preorderTraversal(node.right)
    
    def inorderTraversal(self, node):
        if(not node.left  == None): self.inorderTraversal(node.left)
        print(node, end='')
        if(not node.right == None): self.inorderTraversal(node.right)

    def postorderTraversal(self, node):
        if not node.left  == None : self.postorderTraversal(node.left)
        if not node.right == None : self.postorderTraversal(node.right)
        print(node, end='')

if __name__=="__main__":
    n=int(sys.stdin.readline().strip())

    tree = BinaryTree()

    nodes=[]

    for _ in range(n):
        a,b,c=map(int,sys.stdin.readline().split())
        node=Node(a,b,c)
        # print('data of Node',node)
        # print('data of left_current',node.left)
        # print('data of right_current', node.right)
        nodes.append(Node(a,b,c))

        # abbreviation of above
        # nodes.append(Node(a,b,c))
    # print(nodes)

    # below append is 'only' for complete tree
    # for i in range(int(len(nodes)/2)):
    #     print('idx',i)
    #     print('curNode',nodes[i])
    #     print('leftNode',nodes[i*2+1])
    #     print('rightNode',nodes[i*2+2])
    #     tree.makeRoot(nodes[i],nodes[i*2+1],nodes[i*2+2])

    for node in nodes:
        tree.insert(node)

    print(       '전위 순회 : ', end='') ; tree.preorderTraversal(tree.root)
    print('\n' + '중위 순회 : ', end='') ; tree.inorderTraversal(tree.root)
    print('\n' + '후위 순회 : ', end='') ; tree.postorderTraversal(tree.root)
