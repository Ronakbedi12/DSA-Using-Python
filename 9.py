def checkPalindrome(x):
    temp = x
    rev = 0
    while(temp > 0):
        digit = temp % 10
        temp = temp // 10
        rev = rev * 10 + digit
    if rev == x:
        return True
    else:
        return False
ans=checkPalindrome(121)
print(ans)