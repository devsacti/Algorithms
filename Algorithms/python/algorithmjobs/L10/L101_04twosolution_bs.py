'''
binary search의 구현
1. left, right
2. while 속 if else

#새로만든 bs의 경우 음수 양수 구분이 없어서 이런 현상 발생.
3
-1 9 12
[(-1, -1)]
-1 -1
대비해서 

bs에 
    tmp_sorted_seq=sorted_seq[:]
    tmp_sorted_seq.remove(std)
    idx_left=0
    idx_right=(N-1)-1
    추가했는데 타임리밋넘음!

! while조건을 idx_right-idx_left>=1로 잡으면 left와 right가 포개지지 않을거라고 생각했는데
실제 연산상, int로 내림하면서 깍이고, mid-1을 대입하면서 2칸 이동되는듯,
결국 포개짐,

생각해보니 0일때는 아에 마지막 연산 후 엇나가는 거였음.
그러니까 2로 하면됨. 그런줄 알았는데 실제 연산결과 이래도 결국 포개짐.
3으로 바꾸면 약간 엇나감
left right를 정의를 약간 변형했는데 무한루프

!!겨우겨우 구현했더니 95점에서 멈춤,
겨우겨우 코치님한테 해당 케이스 받아서 보니까,
숫자가 많고 간격이 넓어지면서 
기존 threshold를 아무것도 넘지 못해서
list_candiates에 아무것도 못들어가서 문제였음,
원래라면 어디서 runtime나오는지 알아서 금방해결했을텐데....

일단 threshold 100에서 넘을수없는 수준으로 증가

'''

from collections import deque

def bs(sorted_seq,N, std):

    idx_left=0
    idx_right=(N-1)
    
    while(idx_right-idx_left>=2):

        idx_mid=int((idx_left+idx_right)/2)
        # print('##std, val_mid',std,sorted_seq[idx_mid])

        if(std+sorted_seq[idx_mid]==0):
            return (std, -std)
        elif(std+sorted_seq[idx_mid]<0):
            idx_left=idx_mid+1-1
        elif(std+sorted_seq[idx_mid]>0):
            idx_right=idx_mid-1+1
        else:
            pass
    
    # print( (std, sorted_seq[idx_left]), (std, sorted_seq[idx_right]) )

    candi1_pair=(std, sorted_seq[idx_left])
    candi2_pair=(std, sorted_seq[idx_right])

    if( candi1_pair[0]==candi1_pair[1] or candi2_pair[0]==candi2_pair[1]):
        if(candi1_pair[0]==candi1_pair[1]):
            #
            return candi2_pair
        elif(candi2_pair[0]==candi2_pair[1]):
            #
            return candi1_pair
        else:
            #
            pass
    else:
        val_candi1=abs(sum(candi1_pair))
        val_candi2=abs(sum(candi2_pair))

        if(val_candi1<val_candi2):
            return candi1_pair
        else:
            return candi2_pair  


if __name__=='__main__':
    N=int(input())
    seq=list(map(int, input().split()))

    sorted_seq=sorted(seq)
    # print(sorted_seq)

    deque_seq=deque(sorted_seq[:])
    # print(deque_seq)

    list_candidates=list()
    token_approximate=1

    if(sorted_seq[0]>=1):
        print(sorted_seq[0], sorted_seq[1])
    elif(sorted_seq[-1]<=-1):
        print(sorted_seq[-2], sorted_seq[-1])
    else:
        # min_sum_feature=100
        min_sum_feature=10000000


        while(len(deque_seq)!=0):
            std=deque_seq.popleft()

            result=bs(sorted_seq,N,std)
            # print('#result',result)


            # print('#while, min_sum ', min_sum_feature)
            if(abs(sum(result))<abs(min_sum_feature)):
                min_sum_feature=abs(sum(result))
                #적용되는 기본 로직 상 위 부등호에 =를 넣어야하지만, 문제요구와 정렬된 조건에 따라서 
                #작은 값만 새로 받아도 된다.
                list_candidates.append(result)
            else:
                continue

        
        # print(list_candidates)
        print(list_candidates[-1][0],list_candidates[-1][1])