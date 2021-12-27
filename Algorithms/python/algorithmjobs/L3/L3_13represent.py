if __name__=='__main__':
    N=10

    nums=[]

    for i in range(N):
        nums.append(int(input()))

    mean_nums=int(sum(nums)/len(nums))

    print(mean_nums)

    freqDict={}

    for num in nums:
        freqDict.setdefault(num,0)

    for num in nums:
        freqDict[num]=nums.count(num)

    freqDict_sorted=dict(sorted(freqDict.items()))

    print(freqDict_sorted.items())

    print(max(freqDict_sorted,key=freqDict_sorted.get))
