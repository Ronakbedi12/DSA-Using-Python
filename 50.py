def power_x(x,n):
    # Base case
    if n==0:
        return 1
    # Recursive case
    a = power_x(x , n // 2)
    if n % 2 == 0:
        return a*a
    else:
        return a*a*x
    
def check_Pow(x,n):
    if n>=0:
        return power_x(x,n)
    else:
        return 1/power_x(x,n*(-1))
    
print(power_x(2,10))