n = int(input())
for i in range(-n+1,n,2):
    print(' '*(abs(i)//2),'0'*(n-abs(i)))
