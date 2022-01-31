# tree class를 구현할때, __init__, __str__과같은 특수메소드와, self같은 내장변수가 등장
# 
# class Node:
#     def __init__(self, item):
#         self.data = item
#         self.left = None
#         self.right = None
#
# class BinaryTree:
#     def __init__(self, r):
#         self.root = r
#
# 중요전제; 파이썬 클래스에서 self라는 변수는 '언제나'모든 하위 메서드에 전달된다.
# 이로 인해, 만약
# 
# class Node:
#     def __tempfuc1__():
#         print('i am exclusive')

#     def __init__(self, item):
#         self.data = item
#         self.left = None
#         self.right = None

# 같은 노드 클래스가 코딩된다면, '클래스 선언'은 되지만, instance로 메모리할당 후
# tempfuc1 호출 시, 에러문구로, 이 함수는 아규먼트가 0개인데 1개를 받았다. 라는 에러가 뜬다

# 한편, 자세한 구조나 원리는 모르겠고, 어떻게 보면 역설지이지만
# self는 클래스의 인스턴스화 시, 선행적인 인스턴스로 먼저 형성되어 전달되는걸로 보인다.

# True and False, by the way None
# None is not sub conception of False, it is different at least at start
# so, to code traverse, if not ~ ==none form is needed
# but, after processing 'none==none' or 'not none == none',
#  the result is True or False, so this relavance should be counted 

class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)
'''!!!'''
# 참고로, 아래와 같은 트리클래스는 오직 완전트리만 고려한 형태
# 입력되는 노드들이 언제나 왼쪽 오른쪽이라서,
# 현재 입력받은 노드가 부모의 왼쪽에 붙어야하는지 오른쪽에 붙어야할지
# 판단 및 결정을 안해도 되는 경우에만 작동한다.
# 당연히 이 입력값이 왼쪽오른쪽 규칙성을 보장안하면, 원래와 다르게 잘못만들어짐. 

class BinaryTree:
    def __init__(self):
        self.root=None

    def makeRoot(self, node, left_node, right_node):
        if self.root == None:
            self.root = node
        node.left = left_node
        node.right = right_node

    def preorderTraversal(self, node):
        print(node, end='')
        if(not node.left  == None): 
            self.preorderTraversal(node.left)
        if(not node.right == None): 
            self.preorderTraversal(node.right)
    
    def inorderTraversal(self, node):
        if(not node.left  == None):
            self.inorderTraversal(node.left)
        print(node, end='')
        if(not node.right == None):
            self.inorderTraversal(node.right)

    def postorderTraversal(self, node):
        if not node.left  == None :
            self.postorderTraversal(node.left)
        if not node.right == None :
            self.postorderTraversal(node.right)
        print(node, end='')

if __name__=="__main__":
    tree = BinaryTree()
    #            root=None
    #          2      3 
    #         4 5    6 7

    #init method1
    tree.makeRoot(Node(1),Node(2),Node(3))
    # 별도로 makeroot가 없다면,
    # 어쨌거나 init에서든 어디선가 노드를 연결하는 초기화 함수가 있어야하고
    #tree.root가 노드이고,
    #tree.root.left=1 같은 식으로 일일이 대입
    
    #init method2
    tree2=BinaryTree()
    nodes=[]
    nodes.append(Node('-'))
    nodes.append(Node('*'))
    nodes.append(Node('/'))
    nodes.append(Node('A'))
    nodes.append(Node('B'))
    nodes.append(Node('C'))
    nodes.append(Node('D'))   

    for i in range(int(len(nodes)/2)):
        print(nodes[i],nodes[i*2+1],nodes[i*2+2])
        tree2.makeRoot(nodes[i],nodes[i*2+1],nodes[i*2+2])

    print(       '전위 순회 : ', end='') ; tree2.preorderTraversal(tree2.root)
    print('\n' + '중위 순회 : ', end='') ; tree2.inorderTraversal(tree2.root)
    print('\n' + '후위 순회 : ', end='') ; tree2.postorderTraversal(tree2.root)




