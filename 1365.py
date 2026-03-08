def CountNumber (nums):
    output=[]
    for i in nums:
        count = 0
        for j in nums:
            if j < i:
                count +=1
        output.append(count)
    return output
ans=CountNumber([8,1,2,2,3])
print(ans)