if __name__=='__main__':
    text=input()

    reversed_text=''.join(reversed(list(text)))

    # print(text,reversed_text)

    if(text==reversed_text):
        print('YES')
    else:
        print('NO')