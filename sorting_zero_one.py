x = int(input())

l1 = (int(x) for x in input().split())
l2 =list(l1)
l3 =[]
for ele in l2:
	if (ele ==0):
		l3.append(ele)
for ele in l2:
	if (ele ==1):
		l3.append(ele)
print(l3)
		
		
		