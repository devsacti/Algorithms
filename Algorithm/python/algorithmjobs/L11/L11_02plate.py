import string
from collections import deque

if __name__=="__main__":
    std_str=input()
    len_std_str=len(std_str)
    #std_str의 인덱스, cursor
    cursor_std=0
    # print(std_str)

    dq_via=deque()
    top_dq_via=len(dq_via)-1
    topelement_dqvia=''

    #
    lowercase=string.ascii_lowercase
    #plus
    uppercase=string.ascii_uppercase;allletter=string.ascii_letters

    selected_lower=lowercase[:len_std_str]
    dq_selected=deque(selected_lower)
    # print(dq_selected)

    list_trial=[]
    
    flag=False

    cmds=[]

    while(1):
        #current needed char of std_str
        currentelment=std_str[cursor_std]

        #dq_via의 top구하기 for 목표알파벳 문자열 만들기 위해
        top_dq_via=len(dq_via)-1
        if(top_dq_via==-1):
            topelement_dqvia='*'
        else:
            topelement_dqvia=dq_via[top_dq_via]
        #exit condition 2: needed one is under top
        # print('###',currentelment,topelement_dqvia)
        if(currentelment in dq_via and currentelment!=topelement_dqvia):
            break


        #오직 top만 보자
        # print('##',currentelment,topelement_dqvia)
        if(currentelment==topelement_dqvia):
            #pop of dq_via
            val_pop=dq_via.pop()
            list_trial.append(val_pop)
            # print('#list trial',list_trial)
            # print('pop')
            cmds.append('pop')
            cursor_std+=1
        else:
            #push of dq_via
            top_dqselected=len(list(dq_selected))-1
            if(top_dqselected>=0):
                val_push=dq_selected.popleft()
                dq_via.append(val_push)
                # print(dq_via)
                # print('push')
                cmds.append('push')
            # else:
            #     #상위 exit조건으로 인해 아직 완성되지 않았는데, 거기에 더해
            #     #현 ifelse로 인해 기본적으로 여기는 더이상 popleft할게 없는상황,
            #     #exit condition 3: there is no one to push
            #     break
            #     # 다만 현재 중복이 없는 입력조건 특징상
            #     #  상위 exit condtion2에서  잡힐듯
        
        # 여기서부턴
        # 1차적으로 dq_via topelement에 필요한게 있어서 trial에 붙이고 cursor가 1증가
        # 또는 2차적으론 dq_via 에 새로운 엘리먼트를 보급한 후


        #exit condition 1: std_str complete
        # if( ''.join(list(dq_trial))==std_str ):
        # 위에도 의미상 맞긴한데, 시간소요 다운을 위해 아래와같이 하자
        if(cursor_std>=len_std_str):
            flag=True
            break

    if(flag==True):
        for cmd in cmds:
            print(cmd)
        # print(''.join(list_trial))
    else:
        # print('list_trial',list_trial)
        print('impossible')