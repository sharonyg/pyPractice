import re

def score(file_data):
    
    name_str = re.findall("[A-Z]+", file_data)
    
    names = sorted(name_str)
    li = []
    for index, ele in enumerate(names, 1):
    	val = sum(ord(letter)-64 for letter in ele)
    	li.append(val * index)

    return sum(li)   
    
