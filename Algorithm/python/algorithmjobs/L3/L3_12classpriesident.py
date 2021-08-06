'''

step1
 N, N*N matrix not zeros
 
 make the rendezvous matrix for step2.a

step2 
    a
    check the rendezvous matrix
    학년 레이어에서 반복되는 수를 찾고
    그 수를 가진 학생번호를 찾고
    학생번호의 랑데뷰 매트릭스를 업데이트
    
    b
    또는 일단 학생 기준으로 1학년 반분포에서 자기랑 같은 숫자 만나면 체크
    누가 누구를 만났나는 체크되지 않으니 간결할듯,
    특히 누적이나 몇학년 이란 언제에 조건이 없으니 더욱 적합

    ->fail 왜냐하면 애당초 내 계산과 문법은 애매했지만,
    결과적으로도 3학년때 같은 반인 3명이 모두 cnt가 3으로 제일크지만
    4번학생의 경우 4학년 때 찢어져서 2번학생과도 안면이 생겼지만
    4학년에 대한 연산 시 cnt~가 2라서 누락됨, 학생관점으로 회귀, 일종의 인스타그램

'''

if __name__=='__main__':
    '''step1'''
    N = int(input())

    recordmatrix=[]

    for i in range(N):
        recordmatrix.append(list(map(int,input().split())))

    #print(*recordmatrix,sep='\n')

    inverse_recordmatrix=list(zip(*recordmatrix))

    print(*inverse_recordmatrix,sep='\n')

    '''step2'''
    '''처음에는 4중 for문->2중 ->3중으로 고침
    그만큼 다중for간 관계에 대해서 오해하고 설계해서 오류
    추가로 접근방식도 전환'''

    dictname=dict()

    names=[i+1 for i in range(N)]

    for name in names:
        dictname.setdefault(name,set())

    for num,student in enumerate(recordmatrix,1):
        one, two, three, four, five = student

        #print(num, one,two,three,four,five)

        for num2,element in enumerate(inverse_recordmatrix[0],1):
            if(one==element):
                dictname[num].add(num2)

        for num2,element in enumerate(inverse_recordmatrix[1],1):
            if(two==element):
                dictname[num].add(num2)

        for num2,element in enumerate(inverse_recordmatrix[2],1):
            if(three==element):
                dictname[num].add(num2)

        for num2,element in enumerate(inverse_recordmatrix[3],1):
            if(four==element):
                dictname[num].add(num2)

        for num2,element in enumerate(inverse_recordmatrix[4],1):
            if(five==element):
                dictname[num].add(num2)



    #print(dictname)
    
    #딕셔너리에서 최대 값을 가진 키 찾기 by 컴프리헨션
    #print([k for k,v in dict_aquaintance.items() if max(dict_aquaintance.values()) == v])
    #or
    #print( max(di, key=lambda x: len(di[x]) ) )
    #int에 한하여 print([max(di,key=di.get)])
    #or
    #sort

    print( max(dictname, key=lambda x:len(dictname[x])) )