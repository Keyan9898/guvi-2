n=input()
l=list(map(int,input().split(" ")))
for i in range(len(l)-1):
	if l[i]>l[i+1]:
		l[i]=l[i+1]
	else:
		l[i]=-1
l[len(l)-1]=-1
print(*l)
