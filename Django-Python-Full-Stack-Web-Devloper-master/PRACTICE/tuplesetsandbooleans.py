# Tuples are immutable sequences/mixed datatypes - Both string and tuple are immutable
# Sets are unordered collections of unique elements - it only takes unique elements
# Booleans are just True and False as before


# Booleans

True
False
0
1



# Tuples

mylist = (1,2,3)
print(mylist[0])

mylist = ['a', True, 123]
print(mylist[2])

mylist[0] = 'new'
print(mylist)



# Sets

x = set()

x.add(1)
x.add(2)
x.add(4)
x.add(0.11)
x.add(0.11)
x.add(0.11)
print(x)

converted = {1, 2, 3, 4, 5, 5}
print(converted)


