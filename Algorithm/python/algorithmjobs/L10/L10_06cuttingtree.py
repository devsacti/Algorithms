'''
step1 파이썬의 강점 정렬을 활용

step2
 관점의 전환, 우리가 필요한 건 짜투리의 합인 M인데
 h가 커질수록 그 값이 줄어든다. 
 생각의 편의를 위해 MAX height-h를 새로 정의해도되는데, 여기는 비례가 1쌍뿐이네

+
def check_pass(heights_tree,h):
    # print('h ',h)
    list_h=[h]*len(heights_tree)
    fxy=lambda x,y : x-y if x>=y else 0

    source_treegotten=list(map(fxy,heights_tree,list_h))
    # print(source_treegotten)
    treegotten=sum(source_treegotten)
    # print(treegotten)

    if(treegotten>=M):
        return 1
    else:
        return 0
일케하니까 타임리밋뜸, 더 빨라보이는걸 해보자
'''

def check_pass(heights_tree,h):
    len_heights=len(heights_tree)
    idx_left=0
    idx_right=len_heights-1

    while(idx_right-idx_left>=0):
        idx_mid=int((idx_left+idx_right)/2)

        if(h==heights_tree[idx_mid]):
            #
            limit=idx_mid
            break
        elif(h>heights_tree[idx_mid]):
            #
            # limit=idx_mid
            idx_left=idx_mid+1
        else:
            limit=idx_mid
            idx_right=idx_mid-1

    sum_selected=sum(heights_tree[limit:])

    treegotten=sum_selected-h*(len_heights-(limit))

    if(treegotten>=M):
        return 1
    else:
        return 0

if __name__=='__main__':
    N,M=map(int, input().split())

    heights_tree=list(map(int, input().split()))
    heights_tree=sorted(heights_tree)
    max_h=heights_tree[-1]

    hs=[i for i in range(max_h+1)]

    # print(heights_tree,max_h)
    # print(hs)

    '''
    for h in hs:
        #map and lambda
        fx=lambda x,y : x-y
        source_treegotten=list(map(fx,heights_tree,h))
        treegotten=sum(source_treegotten)

        if(treegotten>=M):
            break
    '''

    idx_left=0
    idx_right=len(hs)-1

    while(idx_right-idx_left>=0):
        idx_mid=int((idx_left+idx_right)/2)

        if(check_pass(heights_tree,hs[idx_mid])==1):
            limit=idx_mid
            idx_left=idx_mid+1
        else:
            idx_right=idx_mid-1
        
    print(limit)

    