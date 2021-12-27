# 순열 구하기
import string
import sys

def permute(depth,result):
    global chars
    global r

    if(depth>=r):
        print(''.join(result))
        return
    else:
        for char in chars:
            if char not in result:
                result[depth]=char
                permute(depth+1,result)
                result[depth]='0'
            else:
                continue


if __name__=="__main__":
    global r
    n,r=map(int,sys.stdin.readline().split())

    samplespace=string.ascii_lowercase

    global chars
    chars=samplespace[:n]
    
    # print(chars)

    depth=0
    result=['0']*r
    permute(depth,result)