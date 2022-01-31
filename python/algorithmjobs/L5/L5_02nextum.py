if __name__=='__main__':
    testcasestojudges=[]

    token=1

    while( token!=0 ):
        testcase = list(map( int, input().split()))
        a1, a2, a3 = testcase

        # print(a1, a2, a3)
        # print()

        #-5 0 -5가 걸려버림, 주어진 예제 말고도,
        # if( sum(testcase)==0):
        #     token=0
        #     break
        if( a1==0 and a2==0 and a3==0):
            token=0
            break

        if( (a1+a3)/2 == a2 and a2-a1 !=0):
            testcasestojudges.append(['AP',a3+(a2-a1)])

        else:
          #등비가 먼저 if로 하게 될 시,0으로 나누게 되면 run time error생김 유의하자.
            testcasestojudges.append(['GP',int(a3*(a2/a1))])

    
    for judge in testcasestojudges:
        print(' '.join(map(str,judge)))