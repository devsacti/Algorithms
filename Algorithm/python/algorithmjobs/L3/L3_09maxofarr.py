import math

'''아래 원점으로부터의 거리는 어떻게 보면 세련됬지만, 문제의 요구(모든 순간 행우선 후 열)
과 딱 맞지않음 왜냐하면 일단 원점으로부터 거리가 같다(행열구분x)다음 이라서
후보가 3개일때 오작동
->일단은 패러프레이징보단 원문그대로 로직을짜보자.'''
def dist_Index(idx):
    #idx = [4,6]
    x,y = idx
    dist=math.sqrt(x**2+y**2)

    return dist

def findIndex_max(maxdictionary):
    globalMax=max(maxdictionary.keys())
    print(globalMax)

    idxs_globalMax=maxdictionary[globalMax]

    #후보들 중 최종 후보를 고르기 위한 단계; 언제나 행우선 그 후 열
    
    #행값을 기준으로 우선 배열, 근데 탐색 로직상 자연스럽게 작은행순으로 들어감
    #sorted_idxs=sorted(idxs_globalMax, key=lambda element: element[0])
    min_row=idxs_globalMax[0][0]
    #행순으로 정렬됬으니 최소행값을 충족하는 애들만 선택
    selected_idxs=[element for element in idxs_globalMax if element[0]==min_row]
    
    #열단위로 정렬
    sorted2_idxs=sorted(selected_idxs,key=lambda element:element[1])

    idx_row_globalMax, idx_col_globalMax=sorted2_idxs[0]
    row_globalMax, col_globalMax=idx_row_globalMax+1, idx_col_globalMax+1
    
    return row_globalMax, col_globalMax

    '''아래는 2프로 부족한 로직, 이유는 맨위 주석'''
    # dists=[]
    # for idx in idxs_globalMax:
    #     #print(dist_Index(idx))
    #     dists.append(dist_Index(idx))
    # ##max(~)
    # min_dist=min(dists)

    #maxdictionary[globalMax]에서 이루어지는 key->value 단계
    # for idx in idxs_globalMax:
    #     if(dist_Index(idx)==min_dist):
    #         fx=lambda x: x+1
    #         row_globalMax, col_globalMax= map(fx,idx)
    #         return row_globalMax,col_globalMax

    #         '''
    #         위 케이스의 경우 100이 8행 9열 또는 9행 8열에 있을때 2개를 뱉어냄
    #         따라서 행단위 탐색을고려해서 리턴해도 되고,
    #         절차성을 원한다면 또 for문돌려야한다.
            
    #         +최소 3개까지 검증하라
    #         '''
        

    # 처음에는 어쩔수없이 지엽적인 케이스 처리부터 시작, 하지만 결국
    # 만날 추후 오류를 생각하면 최대한 제너럴하게해서 분석용이하게

    # if(len(idxs_globalMax)>1):
    #     pass
    # else:
    #     #입력받는 게 리스트래도 이중리스트와 단일을 구분하자
    #     #아래는 구분안해서 불능
    #     # fx=lambda x: x+1
    #     # row_globalMax, col_globalMax= map(fx,idxs_globalMax)
        
    #     # 참고로 길이가 1인데 굳이 for을 쓰는 건 통일성을 위해
    #     for idx in idxs_globalMax:
    #         #print(idx)
    #         fx=lambda x: int(x)+1
    #         row_globalMax, col_globalMax= map(fx,idx)


if __name__=='__main__':
    matrix=[]
    
    maxdictionary={}

    for i in range(9):
        row=[]
        matrix.append(list(map(int,input().split())))
    
    '''step2'''    
    for idx_row, row in enumerate(matrix):
        max_row=max(row)
        idx_col_max=row.index(max_row)
        
        if max_row not in maxdictionary.keys():
            maxdictionary[max_row]=list()
            maxdictionary[max_row].append( (idx_row,idx_col_max) )
        else:
            maxdictionary[max_row].append( (idx_row,idx_col_max) )

    # print(maxdictionary)

    row_globalMax_m,col_globalMax_m=findIndex_max(maxdictionary)
    print(row_globalMax_m,col_globalMax_m)


    # for row in matrix:
    #     print(' '.join(map(str,row)))

