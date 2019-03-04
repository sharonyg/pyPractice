# coding: utf-8
nums = []
with open("sample1.dat") as f:
    for line in f:
        nums.append(line.strip())
        
for i in range(3):
    print max(nums)
    nums.remove(max(nums))
    
