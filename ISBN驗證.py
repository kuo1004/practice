a=list(map(str,input().split()))
def fun2(y):
    b=[0,0,0,0,0,0,0,0,0,0]
    n=0
    for i in range(len(y)):
        if y[i]=='x':
            y[i]=10
        elif type(y[i])!=int:
            y[i]=int(y[i])
    for i in range(len(y)):
        for j in range(0,i+1):
            n=n+int(y[j])
        b[i]=n
        n=0
    return(b)
c=fun2(a)
d=fun2(c)
if d[9]%11==0:
    print("YES")
else:
    print("NO")