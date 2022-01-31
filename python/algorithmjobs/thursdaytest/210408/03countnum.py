import sys

# 에라토스테네스

dict_num={}

if __name__=="__main__":
    n,q=map(int, sys.stdin.readline().split())

    nums=list(map(int, sys.stdin.readline().split()))

    qs=list(map(int, sys.stdin.readline().split()))

    for q in qs:
        if q not in dict_num.keys():
            midresult=nums.count(q)
            dict_num[q]=midresult

            print(midresult)
        else:
            print(dict_num[q])
            