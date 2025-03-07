import numpy as np

#challenge 1: creating a list using range 
x = [*range(0,11,2)]
y = list(range(0,11,2))
print(x==y)

#challenge 2: enumerate the list 
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
range_list = [*(enumerate(names, start=1))]
enum_list = [(i,name) for (i,name) in enumerate(names, start =1)]
print(range_list == enum_list)

#challenge 3: Mapping 
#convert all names to uppercases
names_upper = [*map(str.upper, names)] #.upper() capitalizes all letters
print(names_upper)

nums2 = [[*range(1,6)], [*range(6,11)]]

#challenge 4: Numpy
nums2 = [*range(0,6), [*range(6,11)]]
print(nums2)





