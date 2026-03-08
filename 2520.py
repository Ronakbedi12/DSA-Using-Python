def CountDigit(num):
    temp=num
    count = 0
    while(temp > 0):
        digit = temp % 10
        if num % digit == 0:
            count+=1
        temp = temp // 10
    return count

ans=CountDigit(121)
print(ans)