A=[[1,2,3,4,5,6,7,8,9],[2,4,6,8],[3,6,9]]
output ={}
list_out=[]
for i in range(0,len(A)):
	list_A = A[i]
	list_out.append(list_A[i])
	for j in range(i+1,len(A)):
		list_B = A[j]
		if list_B[j] != list_A[i]:
			list_out.append(list_B[j])
			
	output[list_A[i]] = list_out

print output



