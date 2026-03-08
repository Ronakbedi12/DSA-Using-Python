def Greatest_candies(candies,extraCandies):
    maxcandies=max(candies)
    ans = []
    for i in candies:
        if ( i + extraCandies) >= maxcandies:
            ans.append(True)
        else:
            ans.append(False)
    return ans

final=Greatest_candies([2,3,5,1,3],3)
print(final)