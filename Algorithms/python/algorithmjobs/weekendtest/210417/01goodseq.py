import sys

# token_goodseq는 쓸모없는 갈래를 빠져나오는데 사용
# token_stop은 아에 재귀를 벗어나는 용도로 쓸려고 했는데, 한 갈래 내에서의
# 영향력으론 무용지물 되돌아보면 당연한데 그래서 '전역변수'로 선언해야
# 아규먼트로 전달하는 구조는 결국 재귀구조별 갈래에 제한되더라

def checkgoodseq(depth, result):
    # print(result)
    # 길이가 1이면 별도 액션 없음
    if(depth==0): return True
    else:
        testsample=result[:depth+1]
        # print('testsample', testsample)
        length_testsample=len(testsample)

        unit=1
        # 유효길이내에서 체크
        token_goodseq=True

        while(2*unit<=length_testsample):
            std=testsample[-1-(unit-1):]
            experi=testsample[-1-(2*unit-1):-1-(unit-1)]
            # print('std', std, 'experi',experi)

            if(std==experi):
                token_goodseq=False
                # print('token of good ',token_goodseq)
                break
            else:
                pass
                # print('token of good ',token_goodseq)
            unit+=1

        if(token_goodseq):
            # print('goodseq')
            return True
        else:
            # print('Not goodseq')
            return False

def makeseq(depth,result):
    global token_stop

    # if(depth==0): print('start of makeseq ',depth, result, token_stop)
    # else:
        # print('cur depth',depth)
        # print('result and token stop in makeseq ', result, token_stop)

    if(depth>=N):
        # print('goodseq')
        print(''.join(result))
        token_stop=True
        # print('-------------',token_stop)
        return
    else:
        for item in '123':
            # print('-------------',token_stop)
            if(token_stop): break
            result[depth]=item
            tmp=checkgoodseq(depth,result)
            if(tmp):
                makeseq(depth+1,result)
                result[depth]=0
            else:
                continue

            

if __name__=="__main__":
    N = int(sys.stdin.readline().strip())

    depth=0
    result=[0]*N
    global token_stop
    token_stop=False

    makeseq(depth,result)