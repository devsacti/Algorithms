# Redis and noSQL
noSQL : not only SQL
key - value 모델
in-memory, not disk-based

개인적으로, python dictionary를 외부 DB화 한 느낌

## collection of Redis
collection 이란 자료구조
가령, String, Bitmaps, Hashes, Lists, Sets 등

# download Redis
https://goni9071.tistory.com/473

추가로 최초설치 시 자동 실행 이후, Redis폴더에서 Redis-cli.exe를 클릭하면 cli화면이 뜬다. 
아니면 powersell 등 이요

# tutorial
## string
(example)
> set [key] [value]
OK
> get [key]
[value]


> set hello RedisWorld
OK
> get hello
"RedisWorld"

## list
(example)
> LPUSH mylist A   # now the list is "A"
> LPUSH mylist B   # now the list is "B","A"
> RPUSH mylist A   # now the list is "A","B","A" (RPUSH was used this time)

python의 deque에서 appendleft와 append 와 유사

## HASH
(단건 example)
> HSET [key] [field] [value]
> HGET [key] [field]

(복수 example)
> HMSET [key] [field1] [value1] [field2] [value2]
> HMGET [key] [filed1] [filed2]

파이썬의 이중 딕셔너리와 유사

master_dict = {}

sub_dict={ "i am" : "sub"}
master_dict[key1]=sub_dict

## Set
(example)
> SADD [key] [value1] [value2]
> SMEMBERS [key]

## Sorted Set
> ZADD 2 apple
> ZADD fruit 10 mango
> ZRANGE fruit 0 -1

참고로 여기서 0, -1은 파이선 리스트에서 -1이 맨마지막 인덱스를 의미함과 일맥 상통

# reference
https://medium.com/garimoo/%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%A5%BC-%EC%9C%84%ED%95%9C-%EB%A0%88%EB%94%94%EC%8A%A4-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC-01-92aaa24ca8cc
