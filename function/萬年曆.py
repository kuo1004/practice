y,m=map(int,input().split())
week=['SU','MO','TU','WE','TH','FR','SA']
monthday=[31,28,31,30,31,30,31,30,31,31,30,31]
a=0
def day_year(y):
    A=0
    for i in range(1,y+1):
        if leap_year(i)==1:
            A+=1
        A+=1
    return (A-2)%7
def month_day(y,m):
    x=day_year(y)
    n=0
    for i in range(0,m-1):
        if leap_year(y)==1:
            monthday[1]=29
        n=n+monthday[i]
    return (n+x)%7
    
def leap_year(y):
    if y%4==0:
        if y%100==0:
            return 0
        elif y%400==0:
            return 1
        else:
            return 1
for i in week:
    print(i,end='\t')
print()
b= month_day(y,m)
print('\t'*b,end='')
for i in range(1,monthday[m-1]+1):
    b+=1
    print(i,'\t',sep='',end='')
    if b==7:
        print()
        b=0
    

            