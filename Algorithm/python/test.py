from pandas import DataFrame

origin=[0.1, 0.2, 0.502, 0.902348, None, 0.12908372, 0.1, 0.2, None]

print(id(origin[4]),id(origin[-1]))

data = {'column': origin}
df = DataFrame(data)
domains=set(df['column'])
print(domains)

li_domains=list(domains)
print(id(li_domains[-1]))
print(id(li_domains[-3]))

print(li_domains[-1]==li_domains[-3])
print(li_domains[-1] is li_domains[-3])