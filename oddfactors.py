#oddfactors
n=int(input())
l=[i for i in range(1,n+1,2) if n%i==0]
print(*l)
