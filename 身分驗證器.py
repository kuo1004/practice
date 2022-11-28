def fun1(x1,x2,N):
    return x1+(9*x2)+(8*int(N[0]))+(7*int(N[1]))+(6*int(N[2]))+(5*int(N[3]))+(4*int(N[4]))+(3*int(N[5]))+(2*int(N[6]))+int(N[7])+int(N[8])

n=input()
m=10
for i in range(65,91):
    if i==73:
        m-=1
    if i==79:
        m-=1 
    if i==87:
        m-=1   
    if ord(n[0])==73:
        m=34
        break
    elif ord(n[0])==79:
        m=35
        break
    elif ord(n[0])==87:
        m=32
        break
    elif ord(n[0])==i:
       break
    m+=1
m=str(m)
x1=int(m[0])
x2=int(m[1])
N=n[1:]
P=fun1(x1,x2,N) 

if P%10==0:
    print("CORRECT!!!")
else:
    print("WRONG!!!")