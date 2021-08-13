import sys

def safedp(n):
    global results
    idx_results=n-1

    if(idx_results<3):
        return results[idx_results]
    else:
        # 4 1 0
        # 5 2 0 1
        for i in range(idx_results-2):
            results.append((results[-1]+results[-2]+results[-3])%1000007)
        
        return (results[-1])

if __name__=="__main__":
    n = int(input())
    global results
    
    # 1~2
    # an = a_n-1 + a_n-2 + a_n-3
    results=[]
    # 1 =1
    # 2 = 1+1 or 2
    # 3 = 1+1+1 or 2+1 or 1+2 or 3
    a1=1
    a2=2
    a3=4
    tmp=[a1,a2,a3]
    results.extend(tmp)

    print(safedp(n))