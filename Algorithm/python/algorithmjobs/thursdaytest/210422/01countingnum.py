import sys

dict_q ={}

if __name__=="__main__":
    n,q = map(int, sys.stdin.readline().split())

    nums = list(map(int, sys.stdin.readline().split()))
    qs = list(map(int, sys.stdin.readline().split()))

    for q in qs:
        if(q not in dict_q):
            result=nums.count(q)
            dict_q[q]=result
            print(result)
        else:
            print(dict_q[q])