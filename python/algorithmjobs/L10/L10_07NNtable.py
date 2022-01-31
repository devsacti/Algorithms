# NN단표
# 오후 6:36 2021-04-22
#

import sys

def bs(start, root_end,k):
    # s,e NOT INDEX OF COMPUTER
    s=start
    e=root_end*root_end

    while(e-s>=0):
        # print('start~end',s,e)
        mid=int( (s+e)/2 )
        # print('#mid',mid)

        ##calcul order to compare with k by 'INVERSE function of function that we find'

        # INVERSE function_cand -> table_ of function which algorithm process from table to key 
        # candidates are 1~ 25, and first mid is 13
        # i know that '2' row maybe has 6 mutilples like under the 13; 2,4, 6, 8, 10,12
        # but there is limit at table 5 so we should cut down 
        cntMultiples_perRow=[int(mid//(i)) for i in range(1,root_end+1)]
        cntMultiples_perRow=[root_end if cnt>root_end else cnt for cnt in cntMultiples_perRow]
        orderMid=sum(cntMultiples_perRow)
        # print('orderMid',orderMid)

        if(orderMid==k):
            result=mid
            e=mid-1
            # DO NOT BREAK!
            # cuz, 1~25 is not fit with real component of table
            # exactly, 1~25 has 'more' cand and range of inverse function is not respective between cand
            # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ; parameter
            # 1 2 3 4 5 6   8 9 10    12       15 16          20             25 ; items from NN table
            # - - - - -- - - - -- - - - -- - - - -- - - - -- - - - -- - - - -- 
            # 1 2 3 4 5
            #   2   4   6   8   10
            #     3     6     9       12       15
            #       4       8         12          16          20          
            #         5         10             15             20             25

            # from NN table, which N is 5
            # 1  2  3  4  5
            # 2  4  6  8 10
            # 3  6  9 12 15
            # 4  8 12 16 20
            # 5 10 15 20 25

            # range of cand; order of mid, result of below operation
            # 0 1 3 5 8 10 12 14 15   17       19 21          22             24 ; cnt of front items
            # + + + + + +  +  +  +    +        +  +           +              +
            # 1 1 1 1 1 1  1  1  1    1        1  1           1              1
            #                   16 16 18 18 18 20 22 22 22 ~
            #                        | threshold
            # 12, 13, 14 from cand has same result, those order is 18
            # so to concentrate on 1 cand which exists at NNtable as a THRESHOLD of range
            # by using judge of while, we still don't break
        elif(orderMid<k):
            #result=orderMid를 할수는 있는데 그러면 추가적으로 처리 요구
            s=mid+1
        else:
            result=mid
            e=mid-1

    print(result)
    # result2=checkintable(result,root_end)
    # print(result2)

if __name__=='__main__':
    N=int(sys.stdin.readlin().strip())
    K=int(sys.stdin.readlin().strip())

    bs(1,N,K)
