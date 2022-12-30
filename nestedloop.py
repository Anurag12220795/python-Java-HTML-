n=10
while n>0:
    c=1
    a=1
    b=1
    count=2
    while count<n:
        c=a+a
        a=b
        b=c
        count+=1
    print("fibonacci of %d is %d: ",(n,c))
    n-=1