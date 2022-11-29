def fun1(x):
    if x==1 :
        return 1
    else:
        return x* fun1(x-1)

m,n=map(int,input().split())
v=m-n
y=fun1(m)/(fun1(n)*fun1(m-n))
print(int(y))