
row = list(map(int,input().split()))

row.sort()

print(row[-1]-row[0])