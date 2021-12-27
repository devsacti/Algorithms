from itertools import permutations

# 재귀적으로 만들기
def perm(arr, depth, n, k):
    # depth가 0부터 시작하여 k라면 k개를 모두 뽑은 것이므로 print하고 return
    if (depth == k):
        print(arr)
        return
    for idx in range(depth, n):
        # 각 depth에 대해 남아 있는 것들 중에 모두 뽑아보고,
        # 해당 경우에 대해 재귀적으로 perm 함수를 돌리고,
        # 원상복구 하여 다시 경우의 수를 찾는다
        if(arr[idx] != arr[depth]):
            arr[idx], arr[depth] = arr[depth], arr[idx]
            perm(arr, depth+1, n, k)
            arr[idx], arr[depth] = arr[depth], arr[idx]
        else:
            continue

# 출처: https://countingalaxy.tistory.com/entry/파이썬으로-순열-구현하기 [countingalaxy]

if __name__=="__main__":
    n, r = map(int, input().split())

    ones=[1]*r
    zeros=[0]*(n-r)

    source=ones+zeros

    # print(source)
    
    duplicated_candies=permutations(source)
    print(duplicated_candies)
    print(list(duplicated_candies))
    
    #아쉽게도 set은 앞에껄 우선하지 않는듯,
    #[(0, 1, 0, 1), (1, 1, 0, 0), (0, 1, 1, 0), (1, 0, 1, 0), (1, 0, 0, 1), (0, 0, 1, 1)]
    # nodup_candies=list(set(duplicated_candies))
    # print(nodup_candies)

    result=[]

    for element in duplicated_candies:
        if(element not in result):
            result.append(element)

    # print(result)

    for element in result:
        print(''.join(map(str,element)))
    
    depth=0
    
    perm(source,depth,n,r)


