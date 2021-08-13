class ArrayStack:
    
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

# 수가 문자열로 주어져 있을 때 (몇자리수인지 모르는상태) 
# 각각을 피연산자인 수와 연산자인 기호로 분리해서 리스트로 만드는 작업
# exprStr -> 중위 표현식으로된 수식
def splitTokens(exprStr):
    tokens = []
    val = 0                 # 각 자리 숫자를 담는 변수
    valProcessing = False   # 
    
    for c in exprStr:
        # 빈칸이 들어있으면 그냥 넘어감
        if c == ' ':
            continue
        
        # 숫자를 만나면 10진수로 변환하는 과정
        if c in '0123456789' :
            val = val * 10 + int(c)
            valProcessing = True # 수를 만났으므로 true
        
        # 숫자가 아니라면 (괄호 또는 연산자를 만났다고 간주) 10진수 표현이 끝난것
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            
            valProcessing = False # 지금 10진수를 처리하고있지 않다
            tokens.append(c)
        
    # 마지막 수 처리
    if valProcessing:
        tokens.append(val)
        
    return tokens

def infixTopostfix(tokenList): #중위 표현식을 후위 표현식으로 변환
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for token in tokenList:
        if type(token) is int:
            postfixList.append(token)         
        elif token == ')':
            if token == ')':
                while opStack.peek() != '(':
                #print(opStack.peek())
                    postfixList.append(opStack.pop())
                opStack.pop()
        else:
            if opStack.isEmpty() == False:  
                if prec[opStack.peek()] >= prec[token] and token != '(':
                    postfixList.append(opStack.pop())
                    opStack.push(token)
                elif prec[opStack.peek()] >= prec[token] and token == '(':
                    opStack.push(token)
                else:
                    opStack.push(token)
            elif opStack.isEmpty() == True:
                opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList

def postfixEval(tokenList): #후위 표현식 계산
    opStack = ArrayStack()
    for token in tokenList:
        if type(token) is int:
            opStack.push(token)
        elif token == '*':
            tmp1 = opStack.pop()
            tmp2 = opStack.pop()
            opStack.push(tmp2*tmp1)
        elif token == '/':
            tmp1 = opStack.pop()
            tmp2 = opStack.pop()
            opStack.push(tmp2/tmp1)
        elif token == '+':
            tmp1 = opStack.pop()
            tmp2 = opStack.pop()
            opStack.push(tmp2+tmp1)
        elif token == '-':
            tmp1 = opStack.pop()
            tmp2 = opStack.pop()
            opStack.push(tmp2-tmp1)
    return opStack.pop()


def solution(expr):
    tokens = splitTokens(expr) #문자열을 토큰화 시키는 함수
    print("tokens : ", tokens)
    postfix = infixTopostfix(tokens) #중위 표현식 > 후위 표현식
    print("postfix : ", postfix)
    res = postfixEval(postfix) #후위 표현식 계산
    return res

if __name__ == '__main__':
    quest = '( 13 + 15 ) * ( 16 + 23 )'
    ans = solution(quest)
    print(quest, " = ",ans)