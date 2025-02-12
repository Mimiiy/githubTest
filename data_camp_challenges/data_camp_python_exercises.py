
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


x = [5.7, 4.5]
y = list(map(round, x))
print(y)

