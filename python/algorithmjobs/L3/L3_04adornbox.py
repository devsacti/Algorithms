def getArgs():
    N = int(input())
    colors=list(map(int, input().split()))
    
    return colors

def makeResult(colors):
    colorsdict=dict()
    #usedcolors=list()

    checknum=6

    for color in colors:
        if color not in colorsdict.keys():
            colorsdict[color]=1
        else:
            colorsdict[color]+=1
    #print(colorsdict)

    if(len(colorsdict)>=3 and sum(colorsdict.values())>=6 ):
        for key,val in colorsdict.items():
            if(val>=2):
                checknum-=2
                #usedcolors.append(key)
                colorsdict[key]=0
        
        if( sum(colorsdict.values())>=checknum ):
            print('YES')
        else:
            print('NO')


    else:
        print('NO')



if __name__=='__main__':
    colors=getArgs()
    makeResult(colors)