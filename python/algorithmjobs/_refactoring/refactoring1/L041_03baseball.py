import sys

if __name__=="__main__":
    N=int(sys.stdin.readline().strip())

    answers=[]
    for _ in range(N):
        answer=list(map(int, sys.stdin.readline().split()))
        answers.append(answer)
    
    # print(answers)

    allcases=[(i,j,k) for i in range(1,10) for j in range(1,10) if i!=j for k in range(1,10) if k!=j and k !=i]

    satisfying_case=[]
    for case in allcases:
        token_allpass = True

        for answer in answers:
            std=[int(i) for i in str(answer[0])]
            std_strike=answer[1]
            std_ball=answer[2]
            # print(std, std_strike,std_ball)

            cnt_stike=0
            cnt_ball=0

            for idx_std, val_std in enumerate(std):
                for idx_case, val_case in enumerate(case):
                    if(val_case==val_std):
                        if(idx_case==idx_std):
                            cnt_stike+=1
                        else:
                            cnt_ball+=1

            # print(case,cnt_stike,cnt_ball)
            
            if(std_strike==cnt_stike and std_ball==cnt_ball):
                pass
            else:
                token_allpass=False
                break
        
        if(token_allpass):
            satisfying_case.append(case)


    # print(satisfying_case)
    print(len(satisfying_case))



