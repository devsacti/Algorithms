'''
타입리밋의 문제 해결
최종적으론 그리디를 적용해야하더라도, 
우선 선별과정, 가령 아래의 경우, 합이 0이 되는 최고의 케이스를
먼저 찾아서 시간소요를 최소화하자

+근데, 이렇게 최고의 쌍을 찾는 과정에서 발견되는 최적의 케이스들을 처리할 방법은 없을까

일단 상상으로는 합이 0이되는 짝을 찾는 이진탐색과정을 while로 구성하도,
조건을 l_idx와 r_idx가 같아지면 깨지게 해서 전체를 훑고
도중에 0이 되는 짝을 찾으면 break되게 할 수 있지 않을까

+두번째 풀때는 굳이 양수 음수 안쪼개고 
std랑 정렬된 리스트에 대해서 이진 탐색시켜야할듯
'''

if __name__=='__main__':
    N=int(input())

    vals_soution=list(map(int, input().split()))

    sorted_vals_solution=(sorted(vals_soution))
    # print(sorted_vals_solution)
    #산성 또는 알칼리만 주는 경우, 그리고 나머지

    if(sorted_vals_solution[0]>=1):
        print(sorted_vals_solution[0], sorted_vals_solution[1])
    elif(sorted_vals_solution[-1]<=-1):
        print(sorted_vals_solution[-2], sorted_vals_solution[-1])
    else:
        # print(sorted_vals_solution)
    
        #나도 모르게 놓친 break
        #1. 1과 같거나 크다
        #2. 1을 조건하는 것 중 '첫번째'
        for idx,element in enumerate(sorted_vals_solution):
            # print(idx,element)
            if(element>=1):
                std_idx=idx
                break
        
        # print(std_idx)

        minuss=sorted_vals_solution[:std_idx]
        pluss=sorted_vals_solution[std_idx:]

        # print(minuss)
        # print(pluss)

        bestpair_dict=dict()

        # 처음부터 의도한건 아닌데, minus를 먼저해서 오름차순조건도 충족,
        # 근데 40점이라 어디가 문제인지...
        # 아마도 타임리밋 문제, 그래서 이진탐색과정으로 시간소요 감소 시도

        # min_val_feature = -100
        # for minus in (minuss):
        #     for plus in (pluss):

        #         if(abs(minus+plus)<=abs(min_val_feature)):
        #             min_val_feature=minus+plus

        #             if(minus+plus not in bestpair_dict.keys()):
        #                 bestpair_dict[minus+plus]=list()
        #                 bestpair_dict[minus+plus].append((minus,plus))
        #             else:
        #                 bestpair_dict[minus+plus].append((minus,plus))
        # print(bestpair_dict)
                
        min_val_feature = -100

        
        left_idx_pluss=0
        right_idx_pluss=len(pluss)-1
        '''
        처음에 for문 들어가기 전에 이렇게 정의를 했는데,
         mid_idx의 경우 for문마다 초기화 필요
        left_idx_pluss=0
        right_idx_pluss=len(pluss)-1
        #while에 들어가기 위한 초기값
        mid_idx=-1
        '''

        if(len(pluss)==1):
            for minus in minuss:
                if(abs(minus+pluss[0])<=abs(min_val_feature)):
                    min_val_feature=abs(minus+pluss[0])

                    if(min_val_feature not in bestpair_dict.keys()):
                        bestpair_dict[min_val_feature]=list()
                        bestpair_dict[min_val_feature].append((minus,pluss[0]))
                    else:
                        bestpair_dict[min_val_feature].append((minus,pluss[0]))
                
            key=list(bestpair_dict.keys())[-1]

            # print(bestpair_dict[key][0])

            result_list=sorted(bestpair_dict[key], key=lambda element : element[0])
            # print(result_list)

            for element in result_list[0]:
                print(element, end=' ')
        else:

            for minus in minuss:
                # print('#for',minus)
                token_forbreak=1
                key=-minus

                left_idx_pluss=0
                right_idx_pluss=len(pluss)-1
                #while에 들어가기 위한 초기값이었으나, while별개로 파이썬 특징상 아무거나 할당한걸로도 가능
                mid_idx=-1

                # 처음에는 mid_idx를 결정하는 방식을 모르니,
                # while의 조건을 left_idx_pluss!=right_idx_pluss로 잡았는데
                # 일케하면 영원히 루프, 갱신과정을 다르게 정의해야 쓸수있었다. 
                while(right_idx_pluss-left_idx_pluss>=0):
                    # int는 '내림'이고 이를 유념해야 근사값 짝 찾을 때 오류 피할수
                    mid_idx=int( (left_idx_pluss+right_idx_pluss)/2 )
                    # print('##while',minus ,pluss[mid_idx])

                    if(pluss[mid_idx]==key):
                        print(minus, pluss[mid_idx])
                        token_forbreak=0
                        break
                    elif(key<pluss[mid_idx]):
                        right_idx_pluss=mid_idx-1
                    elif(key>pluss[mid_idx]):
                        left_idx_pluss=mid_idx+1
                    else:
                        pass

                if(token_forbreak==0):
                    # print('check')
                    break

                # left right 양끝을 포함해서 합이 0이되는 짝은 없는 상황, 즉 최고의 쌍이 없는 경우,
                # 최적 쌍을 저장해야. 근데, 이진탐색 구조상 idx가 range를 벗어나니
                # mid_idx를 바탕으로 써야, 경우에 따라 mid_idx가
                # 맨왼쪽 또는 오른쪽에 있고 아래 if는 그 상황별 근사값 정의

                '''뒤늦게 양의 리스트 길이가 1이면 이진탐색이 불성립하는 문제 발견'''
                # 이쯤에도 분기할 수 있지만 의미상 폴문 전에서 분기하기로 결정

                # print('#mid_idx',mid_idx)
                if(mid_idx==0):
                    candi_pair1=(minus, pluss[mid_idx])
                    candi_pair2=(minus, pluss[mid_idx+1])
                else:
                    candi_pair1=(minus,pluss[mid_idx-1])
                    candi_pair2=(minus,pluss[mid_idx])
                # print('#candi',minus,candi_pair1,candi_pair2)
                
                candi_min_feature1=abs(candi_pair1[0]+candi_pair1[1])
                candi_min_feature2=abs(candi_pair2[0]+candi_pair2[1])

                if(candi_min_feature1<candi_min_feature2):
                    candidate_pair=candi_pair1
                elif(candi_min_feature1>=candi_min_feature2):
                    candidate_pair=candi_pair2
                else:
                    pass

                if(abs(candidate_pair[0]+candidate_pair[1])<=abs(min_val_feature)):
                    min_val_feature=abs(candidate_pair[0]+candidate_pair[1])

                    if(min_val_feature not in bestpair_dict.keys()):
                        bestpair_dict[min_val_feature]=list()
                        bestpair_dict[min_val_feature].append(candidate_pair)
                    else:
                        bestpair_dict[min_val_feature].append(candidate_pair)


            # print(bestpair_dict)


            if(token_forbreak!=0):
                key=list(bestpair_dict.keys())[-1]

                # print(bestpair_dict[key][0])

                result_list=sorted(bestpair_dict[key], key=lambda element : element[0])
                # print(result_list)

                for element in result_list[0]:
                    print(element, end=' ')
