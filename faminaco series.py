n=int(input("Enter the number: "))
c=0
a=1
b=1
if n==0 or n==1:
    print("yes")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("It is Fibonacci Number")
    else:
        print("It is not Fibonacci Number")
