'''
link : https://programmers.co.kr/learn/courses/30/lessons/77486

ps3. Impl
vector 형태의 tree로 구현 예정
'''
from collections import defaultdict

def cutting(revenue):
    share=revenue//1
    
    return share
    
def dfs(reversed_tree, child,revenue):
    global dict_name_result
    # 버림 => 줄 거의 소수점을 버리되, 그걸 가질거에 붙여서 정수화
    give_revenue=cutting((revenue*(0.1)))
    get_revenue=revenue-give_revenue
    
    if(child=='center'):
        return
    
    dict_name_result[child]+=(get_revenue)
    # tree 기준 현재 child의 parent
    for parent in reversed_tree[child]:
        print('cur child', child, dict_name_result[child], 'parent',parent, give_revenue)
        dfs(reversed_tree, parent, give_revenue)
    
def solution(enroll, referral, seller, amount):
    reversed_tree=defaultdict(list)
    tree=defaultdict(list)
    
    for child,parent in zip(enroll,referral):
        if(parent=="-"):
            # 이해와 대조를 위한 tree
            tree["center"].append(child)            
            # 역트리
            reversed_tree[child].append("center")
        else:
            tree[parent].append(child)
            reversed_tree[child].append(parent)
    
    keys=list(reversed_tree)
    
    # for key in keys:
    #     print(key,',', reversed_tree[key])
    # print()

    # center는 제외한, 판매원별 수익
    global dict_name_result
    dict_name_result={name : 0 for name in enroll}
            
    for seller,amount in zip(seller,amount):
        # tree 기준 child
        child=seller
        revenue=amount*100
        dfs(reversed_tree, child,revenue)
        
    # print(dict_name_result)
    answer = [val for val in dict_name_result.values()]
    return answer