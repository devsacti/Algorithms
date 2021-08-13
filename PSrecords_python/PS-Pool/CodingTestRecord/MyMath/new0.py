n=int(input())

sample=[i*2 for i in range(1,n+1)]

result = ''.join(map(str,sample))

print(result)

print(result[n-1])