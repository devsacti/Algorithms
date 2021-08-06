if __name__=='__main__':
    operand1=int(input())

    operator=input()

    operand2=int(input())

    if(operator=='+'):
        print(operand1+operand2)
    elif(operator=='-'):
        print(operand1-operand2)
    elif(operator=='/'):
        print(int(operand1/operand2))
    elif(operator=='*'):
        print(operand1*operand2)
    else:
        pass
