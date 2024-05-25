# Scenario 1

# We start by creating a variable named 'node_one' and assign it the value 10
node_one = 10

# We then create another variable 'node_two' and assign it the value of 'node_one'
node_two = node_one

# Printing the values of 'node_one' and 'node_two'. Both should output 10.
print(node_one)
print(node_two)

# Printing the memory addresses of 'node_one' and 'node_two'. 
# Since 'node_two' is a reference to 'node_one', they should have the same memory address.
print(id(node_one))
print(id(node_two))

# Now we create a dictionary object 'node_one_object' with a single key-value pair
node_one_object = {
    "label": "A",
}

# We create another object 'node_two_object' and assign it the value of 'node_one_object'
node_two_object = node_one_object

# Printing the values of 'node_one_object' and 'node_two_object'. Both should output {'label': 'A'}.
print(node_one_object)
print(node_two_object)

# Printing the memory addresses of 'node_one_object' and 'node_two_object'. 
# Since 'node_two_object' is a reference to 'node_one_object', they should have the same memory address.
print(id(node_one_object))
print(id(node_two_object))

# We update the 'label' value of 'node_two_object' to 'B'
node_two_object['label'] = 'B'

# Printing the values of 'node_one_object' and 'node_two_object'. Both should output {'label': 'B'}.
# This is because 'node_two_object' is a reference to 'node_one_object', so when we update 'node_two_object', 'node_one_object' is also updated.
print(node_one_object)
print(node_two_object)

# Printing the memory addresses of 'node_one_object' and 'node_two_object'. 
# The memory addresses remain the same even after the update, demonstrating that the objects themselves have not been duplicated, only referenced.
print(id(node_one_object))
print(id(node_two_object))