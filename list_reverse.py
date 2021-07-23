x = int(input())

l1 = (int(x) for x in input().split())
l2 =list(l1)


k = len(l2)-1
li2=[]
for i in range(k,-1,-1):
	li2.append(l2[i])
print(li2)
