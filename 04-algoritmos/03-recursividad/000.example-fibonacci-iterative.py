def fibonacci_interative(n):
    n0=0
    n1=1
    fib=0
    if(n==0 or n==1):
        fib=n
    else:
        i=2
        while(i<=n):
            fib=n0+n1
            n0=n1
            n1=fib
            i=i+1
    return fib