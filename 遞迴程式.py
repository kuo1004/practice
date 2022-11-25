a=int(input())
def fun1(x):
    if x==1:
        return x+1
    else:
        return fun1(x-1)+fun1(abs(x//2))
print(fun1(a))