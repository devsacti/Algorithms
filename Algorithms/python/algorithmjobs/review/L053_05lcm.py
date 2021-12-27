import math

# math.ceil
# math.floor
# math.trunc

# round

A,B=map(int, input().split())

print( round(A*B/math.gcd(A,B)) )