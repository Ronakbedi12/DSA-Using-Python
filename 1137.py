def fibonacci(n):
    if n == 0 or n == 1:
        return n
    if n < 3:
        return 1
    a=0
    b=1
    c=1
    for i in range(3,n+1):
        next_value=a+b+c
        a=b
        b=c
        c=next_value
    return next_value
ans=fibonacci(6)
print(ans)