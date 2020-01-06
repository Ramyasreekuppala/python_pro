#for loop
i=1
for i in range(0,10):
	print(i,end='')

#for loop
i=1
num=int(input('enter the number:'))
for i in range(i,num):
	print("%d X %d = %d"%(num,i,num*i));

#use of else stmt in for loop
i=1
for i in range(1,10):
	print(i)
	break;
else:print('for loop is exhausted')
print('the loop is broken due to break statement')

#nested loop
i,j=0,0
n=int(input('enter the number of rows u wantto print'))
for i in range(0,n):
	print()
	for j in range(0,i+1):
		print("*",end='')