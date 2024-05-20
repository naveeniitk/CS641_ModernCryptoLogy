while(True):
	n=list(map(str,input().split()))
	if(len(n)>0):
		for j in n:
			if(len(j)==16):
				print(j)
				break