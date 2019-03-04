# coding: utf-8
def readfile(file):
    nums = []
    with open(file) as f:
         for line in f:
             nums.append(line.strip())
    return nums


def find3Max(nums):  
    li = nums[:3]   

    if li[0] < li[1]:
        if li[0] < li[2]:
            if li[1] > li[2]:
                li[1], li[2] = li[2], li[1]
        else:
            li[0], li[2] = li[2], li[0]
            li[1], li[2] = li[2], li[1]
    else:
        if li[0] < li[2]:
            li[0], li[1] = li[1], li[0]
        elif li[1] < li[2]:
            li[0], li[2] = li[2], li[0]
            li[0], li[1] = li[1], li[0]
        else:
            li[0], li[2] = li[2], li[0]       

    for i in nums[3:]:
        if i > li[2]:
             li[0] = li[1]
             li[1] = li[2]
             li[2] = i
        elif i > li[1]:
             li[0] = li[1]
             li[1] = i
        elif i > li[0]:
             li[0] = i

    return li           
