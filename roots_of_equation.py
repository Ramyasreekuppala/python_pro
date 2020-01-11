import square_root
def roots_equn():
    D=float((b*b)-(4*a*c))
    if(D >= 0):
        print("real roots")
        root_1=float((-b-square_root.sqrt(D))/(2*a))
        root_2=float((-b+square_root.sqrt(D))/(2*a))
        print("root1= ",root_1)
        print("root2= ",root_2)
    elif(D < 0):
        print("imaginary roots")

a=int(input("enter the value of a : "))
b=int(input("enter the value of b : "))
c=int(input("enter the value of c : "))
roots_equn()
