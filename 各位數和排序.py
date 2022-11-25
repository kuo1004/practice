def fun1(x):
    x=str(x)
    return int(x[0])+int(x[1])+int(x[2])+int(x[3])

n=int(input())
data=list(map(int,input().split()))
for i in range(len(data)):
    for j in range(i+1,len(data)):
        a=fun1(data[i])
        b=fun1(data[j])
        if a>b:
            data[i],data[j]=data[j],data[i]
        elif a==b:
            if data[i]>data[j]:
                data[i],data[j]=data[j],data[i]
print(' '.join(map(str,data)))