#if statements
x = 100
if(x ==100):print("value of expressionis 100")
print("goodbye!")

#elseif
name='ramya'

if (name!='ramya'):
	print('its not ramya')
else:
	print('its ramya')

print('end-one')

#nested elseif and logical
num=int(input('number:'))

if(num>0):
	print('positive number')
	if(num%2==0):print('even')
	if((num%2==0)or(num%4==0)):print('multiple of 8')
	if((num%2==0)and(num%7==0)):print('multiple of 7')
	else:print('odd')
elif(num<0):
	print('negative number')
elif(num==0):
	print('number is zero')

print('end-two')

#operators
a=10
b=3
c=-7
print(a+b)
print(a-b)
print(a*b)
print(a%b)
print(a/b)
print(a//b)
print(a**b)
print(a//c)#floor values

#bitwise
print('bitwise operations')
a=8#00001000
b=31#00011111
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<2)
print(a>>2)
print(b>>2)
print(b<<2)






