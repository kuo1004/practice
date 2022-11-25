a=int(input())
n=[]
def F(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return F(x-1)+F(x-2)
print(F(a))
    