'''
.가 먼저 계산되야하는 상태로 인해 1개씩 빼는 게 무의미
홀수개씩이나 짝수개씩도 같은 상황,
앞쪽에서 하나씩 뽑아쓰는 거면 모두 결국 뒤 그 뒤 그 뒤뒤 연산자를
살펴야하는 문제 생김,
그러면 그렇게 하면 되긴하는데, 범용성은 있는건가
범용성에 맞추면 후위표기법이랑 스택계산기, 내가 안외워서 그렇지 복잡한건 아니긴했음

한편,
모든 .의 위치를 먼저 파악한뒤 그 좌우 좌표를 따로 저장해서 
미리 .만 먼저 계산하는 것도 생각했는데
간단하지만 범용성은 있나

하지만 일단 난 간단
+
간단해서 좋긴 한데, 길이는 웬만큼 긴듯, 계산기 암기할걸


++
줄일수 있는 for문, 리스트복사 등을 줄였지만, 결국 타임리밋뜸

+ 연산자 관련하여
으레 변수끼리 연산한다음에는 어디에 저장할지의 문제 발생하는데
그리고 이경우 다음 연산을 위해서 이전 정보가 적절한 곳에 저장되야하는데
운좋게 result와 연산결과와 추후 과정사이에 연관이 있어 result에 저장
도 가능인데 그냥 tmp_nums로 해결했다가 다시 tmp_str로 해결


중요주제 범용성

++
찝찝한 계산기는 실패로 넘어갔고,
현재 틀에서 더 줄여보자

.나오면 +-나오기까지 while 돌려서 calcul 과정을 통합해보자
->dessert2


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

    # print('###',sum)

    return sum


def operator(depth, result, limit):
    global nums
    global cnt

    if(depth==limit):
        global list_tmp
        list_tmp=[]
        list_forprint=[]
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
            tmp_str=''
            # . 먼저 정리하고 사용한 숫자와 연산자 빼게 단서 남기기
            for idx in range(n-1):
                # print(idx)
                instant_operator=result[idx]

                #print를 위한 중위표기식 저장
                list_forprint.append(nums[idx])
                list_forprint.append(result[idx])
                if(idx==(n-1)-1):
                    list_forprint.append(nums[idx+1])

                if(instant_operator=='.'):
                    if(tmp_str==''):
                        tmp_str=nums[idx]+nums[idx+1]
                    else:
                        tmp_str+=nums[idx+1]
                    
                    if(idx==(n-1)-1):
                        list_tmp.append(tmp_str)
                else:
                    if(tmp_str==''):                    
                        list_tmp.append(nums[idx])
                    else:
                        list_tmp.append(tmp_str)
                        tmp_str=''

                    list_tmp.append(result[idx])

                    if(idx==(n-1)-1):
                        list_tmp.append(nums[idx+1])

            
            # print('##',list_tmp)

            #남은 게 +-뿐이라 순차 계산 가능
            val_sum=calcul(list_tmp)

            if(val_sum==0):
                cnt+=1
                # print('##',list_tmp)

                if(cnt<=20):
                    print(' '.join(list_forprint))

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
    result=[0]*(n-1)
    limit=(n-1)

    operator(depth,result,limit)
    print(cnt)
    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
