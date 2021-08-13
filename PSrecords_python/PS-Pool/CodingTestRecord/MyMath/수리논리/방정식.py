import sys
input=sys.stdin.readline
import numpy as np

if __name__=="__main__":

    leftmatrix=[]
    rightmatrix=[]

    print('input the row')
    R=int(input().strip())

    print('input the rightmatrix')

    for _ in range(R):
        row=list(map(int,input().split()))
        leftmatrix.append(row)
    np_lmatrix=np.array(leftmatrix)

    print('input the leftmatrix')

    for _ in range(R):
        row=list(map(int,input().split()))
        rightmatrix.append(row)
    np_rmatrix=np.array(rightmatrix)

    print('-r-')
    print(np_lmatrix)
    print('-l-')
    print(np_rmatrix)

    print('-inversed right-')
    inverse_np_lmatrix=np.linalg.inv(np_lmatrix)
    print(inverse_np_lmatrix)

    print('-result from a, b by sol-')
    result=np.linalg.solve(np_lmatrix,np_rmatrix)
    print(result)
    print('-result from a, b by inv-')
    result=np.dot(inverse_np_lmatrix,np_rmatrix)
    print(result)