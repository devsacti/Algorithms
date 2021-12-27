import sys
import itertools

if __name__=="__main__":
    N=int(sys.stdin.readline().strip())

    answers=[]

    for _ in range(N):
        answer=list(map(int, sys.stdin.readline().split()))
        answers.append(answer)
    
    # print(answers)

    allcases=list(itertools.permutations('123456789',3))
    # print(allcases, len(allcases))

    satis_cases=[]
    for case in allcases:
        token_allpass=True

        for answer in answers:
            std_record=[element for element in str(answer[0])]
            std_strike=answer[1]
            std_ball=answer[2]

            experi_strike=0
            experi_ball=0

            for idx_std, val_std in enumerate(std_record):
                for idx_case, val_case in enumerate(case):
                    if(val_case==val_std):
                        if(idx_case == idx_std):
                            experi_strike+=1
                        else:
                            experi_ball+=1
            

            if( experi_strike == std_strike and experi_ball == std_ball):
                pass
            else:
                token_allpass=False
        
        if(token_allpass):
            satis_cases.append(case)

    print(len(satis_cases))

