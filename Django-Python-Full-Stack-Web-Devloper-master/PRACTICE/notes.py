# Given the string
s = 'django'
# use indexing to print out the following:
# 'd'
print(s[0])
# 'o'
print(s[-1])
# 'djan'
print(s[0:4])
# 'go'
print(s[4:])

# Bonus : Use indexing to reverse the string

# Given this nested list:
l = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"
l[2][2] = 'Goodbye'
print(l)

# Using keys and indexting, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
# print(d3['k1']['nest_key'][1])
print(d3['k1'][0]['nest_key'][1])


# Use a set to find the unique values of the list below:

mylist = {1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3}
print(mylist)

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"




