def Subtract_Product_and_Sum(n):
    temp = n
    prod = 1
    sum = 0
    while(temp > 0):
        digit = temp % 10
        prod = prod * digit
        sum = sum + digit
        temp = temp // 10
    return prod - sum

ans=Subtract_Product_and_Sum(234)
print(ans)