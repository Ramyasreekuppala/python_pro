def leap_year():
    if((year%100!=0 and year%4==0) or year%400==0):
        print('entered year is leap year')
    else:
        print('entered year is not leap year')

year=int(input("enter the year: "))
leap_year()
