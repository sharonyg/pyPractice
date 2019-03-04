
def is_perfect(x):

    num = sum(i for i in range(1, x/2+1) if x%i == 0)
    
    return num == x
