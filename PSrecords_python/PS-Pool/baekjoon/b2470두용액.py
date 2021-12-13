'''
ps1. accurate comprehension
ps1.1. analysis

ps1.2. drawing pattern, exception
pattern1 본문의 특성값 개념을 그대로 bs를 구현하려고 했지만, 처음 도출된 값과 비교해서
왼쪽으로 갈지, 오른쪽으로 갈지 결정할 값이 마땅치 않음
=> 주어진 값중에 그런 것이 없다면, 좌우를 살펴서 이동할수있다!,
이를 pattern2에 혼용

pattern2 우선 Ideal 상황을 가정하고 근사화!+ Empircal!
std와 동일하거나 유사한 값을 찾을려고 노력해보면,
기준과 타겟의 합의 절대값, 즉 특성값이 0이면 스탑

당장 수학적 설명은 모르겠다! nums 정렬 후 기준값마다 특성값 나열하면 오른쪽으로 증가한다.
일단 최초 정렬을 통해 오른쪽으로 갈수록 양수이나 절대값측면에서는 알수없다.
이부분이 혼동이나 어쨌거나 특성값은 abs(std)+ abs(experi)가 아니다.
abs(std+experi) 이므로, experi가 증가할수록 특성값의 이전, 원시값이 커지므로 절대값도 커진다!

=> 전체적인 패턴이 아니었음. 음수+양수인 경우에 한해서 성립하는 패턴이었음
반례)
std = -99 , nums=[-99, -2, -1, 4, 98]
다만, 결과값이 양의 이차함수 꼴임 U패턴, 

종합해보니, 위 성질로 인해서 따로 left, right로 최소값하면 됨        

ps2. utilizing and integration of computer algorithms
ps2.1.

!! exception
언제나 점이 3개 아니라서, 별도의 예외처리가 필요하다. 2개에 따른 비교 혹은 3개에 따른 비교를
세분화하거나, 리스트가 증가하는지 감소하는지 체크필요.


ps2.2.

ps3. Impl
'''
def bs(std,nums,s,e):

    std_s=s
    std_e=e
    print(nums,s,e)

    bestpair_index=-1
    
    while(s<=e):
        mid=(s+e)//2
        print('cur',s,'mid',mid,'e',e)
        
        # custom part
        experi_val=nums[mid]
        experi_feature_val = abs(std + experi_val)

        # left, right for direction
        left_mid=mid-1
        print('left mid',left_mid)
        if(left_mid<std_s):
            # 패턴상 맨 특성값 리스트에서 맨왼쪽이 제일 작은 경우로서, mid가 최적
            bestpair_index=mid
            print('ck')
            break
        else:
            left_experi_val=nums[left_mid]
            left_experi_feature_val = abs(std + left_experi_val)
        
        right_mid=mid+1

        if(right_mid>std_e):
            # 패턴상 맨 특성값 리스트에서 맨왼쪽이 제일 작은 경우로서, mid가 최적
            bestpair_index=mid
            break
        else:
            right_experi_val=nums[right_mid]
            right_experi_feature_val = abs(std + right_experi_val)

        
        print(left_experi_feature_val, experi_feature_val,right_experi_feature_val)

        # finding minimum extreme value
        if(left_experi_feature_val<experi_feature_val<right_experi_feature_val):
            bestpair_index=mid
            e=mid-1
        elif(left_experi_feature_val>experi_feature_val>right_experi_feature_val):
            bestpair_index=mid
            s=mid+1
        else:
            bestpair_index=mid
            break

    return bestpair_index
        

if __name__=="__main__":
    
    n=int(input())
    
    nums=list(map(int,input().split()))
    
    nums.sort()
    
    answer=list()
    
    # start index, end index
    s=0
    e=len(nums)-1
    
    for std in nums:
        print('##',std)
        print(nums[bs(std,nums,s,e)])
        