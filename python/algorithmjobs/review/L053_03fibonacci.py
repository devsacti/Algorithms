import sys

# 순수한 형태의 재귀구조
# def fibonacci(n):
#     if(n==0):
#         return 0
#     elif(n==1 or n==2):
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# python은  dp 개념 필수


if __name__=="__main__":
    n= int( sys.stdin.readline().strip() )

    fibo_sequences=[0,1]
    # 재귀는 아니고 순수하게 dp개념만 활용
    if(n<2):
        print(fibo_sequences[n])
    else:
        for i in range(n-1):
            fibo_sequences.append(fibo_sequences[-1]+fibo_sequences[-2])
        
        print(fibo_sequences[-1])

