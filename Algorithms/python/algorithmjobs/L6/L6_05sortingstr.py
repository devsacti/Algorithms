if __name__=='__main__':
    n=int(input())

    texts=[]

    for i in range(n):
        texts.append(input())

    texts.sort()

    for text in texts:
        print(text)