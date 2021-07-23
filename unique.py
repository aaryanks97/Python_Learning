x = int(input())

l1 = (int(x) for x in input().split())
l2 =list(l1)
l3 = l2

k = len(l2)


for i in range(0,k):
	count = 0
	for j in range(0,k):
		if (l2[i]==l3[j]):
			count = count+1
	if (count==1):
		print(l2[i],end='')
