# myfloat = 1.0
# myint = 1

# result = myfloat == myint
# print(result)

# Bisa dicompare kalo dibikin gini
integer_value = (5)
string_value = ord("a")
result = integer_value < string_value
print(result)  
# Atau gini
integer_value = str(5)
string_value = ("a")
result = integer_value < string_value

print(ord('a'))
print(ord('A'))

my_list = ['apple', 'banana', 'orange']

# Using the join method to concatenate list elements into a string
result_string = ', '.join(my_list)
print(result_string)
