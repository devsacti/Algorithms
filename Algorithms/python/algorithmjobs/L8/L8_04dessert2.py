'''
dessert1 구조로 피연산자 1개, 연산자 1개 업데이트될때마다 합산해서 연산부하를 좀 줄여볼려고,
했는데, 연산자가 .일때와 아닐때로 처리하는 ifelse에서 1+2+ 형태로 미완성 식이 중간과정에
생기고, 분기 갈래마다 처리를 해줘야하는데, 마지막 부호 때고 eval 후 마지막 부호 합산해봄
근데 . 들어가는 순간 중간 eval과정이 너무 복잡해짐

while 형태로 변환
추가로 count도 굳이 14개 세기 전에 8개 되는 순간 토큰 변환식으로 축소
'''

import time

def calcul(list_tmp):
    sum=int(list_tmp[0])
    len_list_tmp=len(list_tmp)

    idx1=1
    idx2=2
    #while 뒤쪽에 연산 붙을 시 인정되야할 다음 시행의 특징을 고려해서 조건식 짜야
    while(idx1!=len_list_tmp):
        operator=list_tmp[idx1]
        if(operator=='+'):
            sum+=int(list_tmp[idx2])
        elif(operator=='-'):
            sum-=int(list_tmp[idx2])
        else:
            pass
        idx1+=2
        idx2+=2

    print('###',sum)

    return sum


def operator(depth, result, limit):
    global nums
    global cnt

    if(depth==limit):

        #join마저 없애기 위해
        list_forprint=''
        # print(result)
        # cnt=result.count('.') 전체 시행마다 발생하는데 이게 +2초정도
        # tmp_nums=nums[:]
        token_skip=0
        cnt_pu=0
        for op in result:
            if(op=='.'):
                cnt_pu+=1
                if(cnt_pu>limit/2):
                    token_skip=1

        if(token_skip):
            pass
        else:
            # pass 단순 if else만 돌리면 8초대, 여기서부터 이미 타임리밋인지 아닌지 모르겠음


            # . 먼저 정리하고 사용한 숫자와 연산자 빼게 단서 남기기
            # idx 0~(n-1)-1
            for idx in range(n-1):
                # print(idx)
                instant_operator=result[idx]

                #print를 위한 중위표기식 저장
                list_forprint+=nums[idx]
                list_forprint+=' '+result[idx]+' '
                if(idx==(n-1)-1):
                    list_forprint+=nums[idx+1]
                print('origin', list_forprint)

            #idx와 idxwhile의 갱신 문제로 분리
            list_tmp=[]
            tmp_str=''
            idx_while=0

            while(idx_while<=(n-1)):
                instant_operator=result[idx_while]
                
                if(instant_operator=='.'):
                    token_next=0
                    while(result[idx_while]=='.'):
                        print(list_tmp)
                        if(token_next==1):
                            tmp_str+=nums[idx_while+1]
                        else:
                            tmp_str=nums[idx_while]+nums[idx_while+1]
                            token_next=1
                        print('tmp_str',tmp_str)

                        idx_while+=1
                        if(result[idx_while]!='.'):
                            list_tmp.append(tmp_str)
                            print(list_tmp)
                            # tmp_str=''
                    

                    # if(idx_while==(n-1)-1+1):
                    #     list_tmp.append(tmp_str)
                    #     break

                else:
                    print(result[idx_while], tmp_str)

                    if(result[idx_while]==0):
                        break
                    else:
                        if(tmp_str==''):
                        
                        else:
                            list_tmp.append(result[idx_while])
                            list_tmp.append(nums[idx_while+1])
                            tmp_str=''
                            idx_while+=1

            
            print('##',list_tmp)

            #남은 게 +-뿐이라 순차 계산 가능
            val_sum=calcul(list_tmp)

            if(val_sum==0):
                cnt+=1
                # print('##',list_tmp)

                if(cnt<=20):
                    print(list_forprint)

    else:
        for element in ('+','-','.'):
            result[depth]=element
            operator(depth+1, result,limit)
            result[depth]=0

if __name__=="__main__":
    start = time.time()  # 시작 시간 저장

    n=int(input())

    global nums
    nums=[str(i) for i in range(1,n+1)]
    # print(nums)

    global cnt    
    cnt=0

    global list_tmp
    list_tmp=list()

    depth=0
    #추후 while 조건문을 위해 1더함, 생각해보면 길이가 다른 리스트 사용시 맞춰주면 좋은듯
    result=[0]*((n-1)+1)
    limit=(n-1)

    operator(depth,result,limit)
    print(cnt)
    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
