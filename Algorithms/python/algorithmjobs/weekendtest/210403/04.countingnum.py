import sys

if __name__=="__main__":
    n,q=map(int,sys.stdin.readline().split())
    
    nums=list(map(int,sys.stdin.readline().split()))
    qs=list(map(int,sys.stdin.readline().split()))

    answers=dict()
    for q in qs:
        if q not in answers.keys():
            result=nums.count(q)
            print(result)
            answers[q]=result
        else:
            print(answers[q])