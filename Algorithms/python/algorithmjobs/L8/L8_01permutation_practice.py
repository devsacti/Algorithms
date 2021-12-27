# 원래는 r이 뎁스를 조절하는 변수인데, 
# 상상대로 r이 감소는 하는데 뭔가 의도보다 빨리 0이 됬고 다시 2로 리셋은 되는데 
# 이 리셋이 내가 생각한대로 다음 단계에서 되지 않기 때문에 무한반복
# +자세히 보니, 일단 vid_used 가 초기화는 되는데, 알수 없는 재귀구조 속에서 제역할 안됨.

# 근데, 원인 구조가 이해안되서
# 맘대로 안되서 limit_depth 선언, 재귀모델링 시 좋은듯

# def recur_permutation(via_candidates, via_used,r, origin_r,limit_depth):
#     print('\n limit_depth  ', limit_depth)
#     print(via_candidates,via_used,r, origin_r)

#     for alpha in via_candidates:
#         if(alpha not in via_used):
#             print('-',alpha,'-',end='')
#             via_used.append(alpha)
#             print('\nin for ',via_used,r, origin_r)
#         else:
#             continue
        
#         위 else가
#         내가 간과한 논리 부분, for문의 첫번째 케이스가 if를 충족하지 않은 상황
#         에 대해서 별도의 지시가 없었고 print없이 r로 넘어간것
        
#         r-=1
#         print('\n r ',r)
#         if(r==0):
#             #end of recurrence by 'enter' in terminal
#             print('here is problem part')

#             via_used=[]
#             r=copy.deepcopy(origin_r)
#             # do nothing or return
#             # do nothing -> NO!NO!NO!NO!NO!NO!NO!NO! 여기는 폴문 안 이니까
#             # 아무것도 안함은 continue
#             continue
#         else:
#             limit_depth+=1
#             if(limit_depth==15):
#                 exit(0)
#             recur_permutation(via_candidates,via_used,r,origin_r,limit_depth)
         

# def permutationfunction(candidates,used,r):
#     via_candidates=copy.deepcopy(candidates)
#     via_used=copy.deepcopy(used)
#     origin_r=copy.deepcopy(r)

    
#     # 1. 이전에 사용한지 아닌지를 확인 후 뱉기; 시간복잡도 증가할듯, 이것도 뭐 쉘로우카피
#     # 2. 이전에 사용한 거 아에 빼서 주기; 쉘로우카피의 문제

#     # 1에 내 사고습관이 더 익숙한것같으니 감수, 지금은 완벽보단 빈틈없이
              
#     recur_permutation(via_candidates,via_used,r,origin_r,1)


# +로직은 문제 없었는듯하다, 내가 로직을 곡해했을뿐,
# 예시에서 a가 나오는동안 뒷자리가 변화한다->'나오는동안~' 언어논리적인 판단을
# 컴퓨터과학적으로 옮길때, a가 매번 반복되는 동안인데,

# 내 언어대로 코딩을 하면,
# ab
# ac
# ad가 아니라

# abcd
# a가 나오는 동안 bcd가 나오는 것이다. 더불어 쉘로우 카피의 문제도 따라오고,


from string import ascii_lowercase
import copy

def permutationfunction(current,r,candidates,result_idx):
    dpcp_result_idx=copy.deepcopy(result_idx)

    if(current>=r):
        #
        for idx in dpcp_result_idx:
            print(candidates[idx],end='')
        print()
        return 0
    else:
        for idx in range(r):
            if(idx not in dpcp_result_idx):
                dpcp_result_idx.append(idx)
                permutationfunction(current+1,r,candidates,dpcp_result_idx)
                dpcp_result_idx=[]


if __name__=='__main__':
    n, r = map(int, input().split())

    #alphabets='abcdefghijklmnopqrstu'
    alphabets=list(ascii_lowercase)
    # print(alphabets)

    #운좋게 문자열 인덱스가 0부터 시작하니까, 아래코드가 의도대로 돌아가는데,
    # 의미를 살리자면
    # alphabets[:(n-1)+1]이다
    candidates=alphabets[:n]

    '''step2 이해단계'''
    '''
    실로 복잡한 재귀구조 구현을 건너뛰고, 아래처럼 코딩가능, 파이썬의 강점 기억하자
    다만 이번 판에서는 내가 저 리스트컴프리헨션 명령어를 통해 호출되는 재귀구조를 구현해야 한다.
    
    참고로 정말 3~4일에 걸쳐서 못풀어서 개좆같았는데,
    정답을 살펴보니, 올바른 재귀구조 틀은 잡은 건 스스로 대견하다.
    '''

    # permutation=[[i,j] for i in candidates for j in candidates if j!=i]
    # print(permutation)
    # 이중 폴문을 위와같이 축약->3중, 4중이 되는 구조를 상상해야, 즉 재귀단계마다 폴문이 있어야하지 않을까

    # for element in permutation:
    #     print(''.join(element))
    '''적용'''
    current=0
    result_idx=[]

    token=permutationfunction(current,r,candidates,result_idx)