a,n=map(int,input().split())
def power(a,n):
    if n==0:
        return 1
    else:
        return a*(power(a,n-1))
def power2(a,n):
    if n==0:
        return 1
    elif n%2==1:
        return a*power2(a,n-1)
    else:
        return power2(a,n/2)*power2(a,n/2)
print(power(a,n))
print(power2(a,n))