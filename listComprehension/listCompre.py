def listCompre(end):
    x = [-i**2 if i%2 == 0 else i**2 for i in range(1, end)]
    ans = sum(x)
    return ans
