if __name__=='__main__':
    text1=input()
    text2=input()

    result=text1.find(text2)

    if(result!=-1):
        print('YES')
    else:
        print('NO')