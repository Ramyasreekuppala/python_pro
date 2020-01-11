from number import numbers
def sum():
    global i
    i=0
    global s
    s=0
    while(i<=10):
        s=s+i
        i=i+1
    print("sum= ",s)
sum()
def avg():
    avg=s/10
    print("average of first ten natural numbers= ",avg)
avg()
def sqn():
    sum=0
    i=0
    while(i<=10):
        sum=sum+int(i**2)
        i=i+1
    print("sum of squares of first ten natural numbers ",sum)
sqn()
def cubn():
    sum=0
    i=0
    while(i<=10):
        sum=sum+int(i**3)
        i=i+1
    print("sum of cubes of first ten natural numbers ",sum)
cubn()
def sum_num():
    sum=0
    m=int(input("enter the value of m= "))
    n=int(input("enter the value of n= "))
    while(m<=n):
        sum=sum+m
        m=m+1
    print("sum of the numbers between"+str(m)+"and"+str(n)+"is"+"=",sum)
sum_num()
def sqr_num():
    sq_sum=0
    m=int(input("enter the value of m= "))
    n=int(input("enter the value of n= "))
    while(m<=n):
        sq_sum=sq_sum+int(m**2)
        m=m+1
    print("sum of squares of  the numbers between"+str(m)+"and"+str(n)+"is"+"=",sq_sum)
sqr_num()
def cubes_sum():
    cube_sum=0
    m=int(input("enter the value of m= "))
    n=int(input("enter the value of n= "))
    while(m<=n):
        cube_sum=cube_sum+int(m**3)
        m=m+1
    print("sum of cubes of  the numbers between"+str(m)+"and"+str(n)+"is"+"=",cube_sum)
cubes_sum()
    
    
        
