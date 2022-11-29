m,n=map(int,input().split())
def gcf1(m,n):
    x=0
    for i in range(1,min(m,n)):
        if m%i==0 and n%i==0:
            x=i
    return x
print(gcf1(m,n))