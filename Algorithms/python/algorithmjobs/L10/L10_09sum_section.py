'''
greedy하게 풀지, parameter쓸지 고민할때,
변수 범위 필수 체크

이 경우 n이 겁나크니까 대충 후자
->wrong!!!1

i가 겁나 커서 막연히 전체 구간 훑으면 큰일 날쭐 알았는데,
n자체는 작고 구간이 일정한 간격(1)로 생성되서 이런 패턴에 근거하면
비록
 o(n)이지만 큰 타격이 없고, 그냥 전체 구간 훑어도된다.

 한편, 시간복잡도를 고민해서 정렬의 필요성을 가늠해야.

step1

step2
 느낌상 starts들에 대해서 우선 bs해서 쓸모없는 구간 버리고,
 다시 유의미한 section들 중 end로 정렬 및 분류해서
 val_mid의 번째를 찾아서 k가 추정하는 것으로 보임

 +
 parameter bs의 문제 발견,
 만약 4 5 5 5 5 6 6 ~ 10와 같은 상황에서 대개 실제로 서로다른 idx를 가지는 5의 문제를
 위해 왼쪽으로 좁혀질때만 저장하는데
 만약 오른쪽으로'만' 올라가다가 결국 mid가 10이될때,
 result 저장을 왼쪽으로갈때만 저장하게 했을때,
 결과가 비어있는 현상,

 NN테이블에서는 운좋게 피해감
 ->가 아니라 같아질때 if문에서 해결이 되야하는데?

'''

if __name__=='__main__':
    n=int(input())

    sections=[]

    #파라미터들은 min_s~max_e가 될듯
    min_s=1000000000
    max_e=1

    for i in range(n):
        s, e = map(int, input().split())

        if(s<=min_s):
            min_s=s
        
        if(e>=max_e):
            max_e=e

        sections.append( (s,e) )

    i=int(input())

    # print(sections, min_s, max_e)

    start_sorted_sections=sorted(sections, key=lambda x : x[0])


    while(max_e-min_s>=0):
        val_mid=int( (max_e+min_s)/2 )
        # print('val_mid', val_mid)
        candi_i=0

        # start가 val_mid보다 커서 0개인 구간을 누락시키자, 즉 val_mid가 start보다 왼쪽 인경우
        idx_s_starts=0
        idx_e_starts=n-1
        while(idx_e_starts-idx_s_starts>=0):
            # print('#',idx_s_starts,idx_e_starts)
            idx_mid=int(  (idx_e_starts+idx_s_starts)/2  )

            if(start_sorted_sections[idx_mid][0]==val_mid):
                critical_idx=idx_mid
                idx_s_starts=idx_mid+1

            elif(start_sorted_sections[idx_mid][0]<val_mid):
                #
                critical_idx=idx_mid
                idx_s_starts=idx_mid+1
            elif(start_sorted_sections[idx_mid][0]>val_mid):
                #
                idx_e_starts=idx_mid-1
            else:
                pass

        # print('#',critical_idx)
        nozero_start_sorted_sections=start_sorted_sections[:critical_idx+1]
        # print('#',nozero_start_sorted_sections)

        # end에 따라서 1개가 되더라도
        # start가 일단 val_mid와 같거나 크니까 일단 구간안에는 들어감, 
        # 결과적으로 val_mid와 같거나 작은 값이 배열 S에 몇개 있는지 뱉음
        for section in nozero_start_sorted_sections:
            start=section[0]
            end=section[1]
            if(end<val_mid):
                candi_i+=end-start+1
            else:
                candi_i+=(val_mid-start)+1

            # print(candi_i)

        # print('idx:i 와 배열 s 속 이하 갯수',i,candi_i)
                
        #위에서 산출된 건 '개'이지 idx가 아니므로 경험적으로 -1
        if((candi_i-1)==i):
            #
            result=val_mid
            max_e=val_mid-1

        elif((candi_i-1)>i):
            #
            result=val_mid
            max_e=val_mid-1
        else:
            min_s=val_mid+1

    print(result)



