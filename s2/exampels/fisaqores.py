a = int(input())
b = int(input())
c = int(input())
x = max((a,b,c))
n = min((a,b,c))
s = sum((a,b,c))
med = s - x - n
if n**2 + med**2 == x**2:
    print('YES')
else:
    print("NO")