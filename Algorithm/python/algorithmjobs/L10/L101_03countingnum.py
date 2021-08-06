if __name__=='__main__':
    n, q = map(int,input().split())

    seq=list(map(int, input().split()))

    quests=list(map(int, input().split()))

    #에라토스.테네스의 체 개념 활용

    count_dict={}

    for quest in quests:
        if(quest not in count_dict.keys()):
            result=seq.count(quest)
            print(result)
            count_dict[quest]=result
        else:
            print(count_dict[quest])