# Define variables
x = 5
y = 10
z = 15

# and operator
print(x < y and y < z)  # True because both conditions are True

# or operator
print(x < y or x > z)   # True because at least one condition is True

# not operator
print(not(x < y))       # False because the condition x < y is True, but not operator negates it to False
