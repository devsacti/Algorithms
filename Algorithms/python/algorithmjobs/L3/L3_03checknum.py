def getArgs():
    #N, S = map(int,input().split())
    seq=list(map(int, input().split()))
    
    return seq

def makeQualificationNum(seq):
    squares=[item**2 for item in seq]
    QualificationNum=sum(squares)%10

    return QualificationNum



if __name__=='__main__':
    seq=getArgs()
    QualificationNum=makeQualificationNum(seq)

    print(QualificationNum)
