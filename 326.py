def powerThree(n):
    if n==0:
        return False
    if n==1:
        return True
    if n % 3!=0:
        return False
    return powerThree(n//3)
ans=powerThree(6)
print(ans)