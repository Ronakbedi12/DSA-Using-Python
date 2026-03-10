def powerTwo(n):
    if n==0:
        return False
    if n==1:
        return True
    if n%2!=0:
        return False
    return powerTwo(n//2)
ans=powerTwo(8)
print(ans)