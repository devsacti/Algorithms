def decimalcounter(row):
    cnt_two=0
    cnt_five=0

    for element in row:
        casefortwo=element
        while(casefortwo>=1):
            if(casefortwo%2==0):
                casefortwo=casefortwo//2
                cnt_two+=1
            else:
                break

        caseforfive=element
        while(caseforfive>=1):
            if(caseforfive%5==0):
                caseforfive=caseforfive//5
                cnt_five+=1
            else:
                break

    return cnt_two,cnt_five

if __name__=='__main__':
    n, m = map(int, input().split())

    # molecular=[i for i in range(1,n+1)]
    # denominator1=[i for i in range(1, m+1)]
    # =>
    molecular=[i for i in range(n-m+1,n+1)]
    denominator=[i for i in range(1,m+1)]
    #print(molecular,denominator)

    two_m, five_m = decimalcounter(molecular)
    two_d, five_d = decimalcounter(denominator)
    
    rest_two=two_m-two_d
    rest_five=five_m-five_d

    #print(rest_two,rest_five)

    if(min(rest_two,rest_five)>=0):
        print(min(rest_two,rest_five))
    else:
        print(0)