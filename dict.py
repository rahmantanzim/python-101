my_dict = {
    "name" : "Rahman"
}
print(f"dictionary with a string key: {my_dict}")
print("^" * 20) 

# tuple as the key

inventory = {}

location_key = ('building 2', 'room 9')

inventory[location_key] = 120

print(f"Inverntory for {location_key} : {inventory[location_key]}") 

#List comprehensions:

#traditional for loop:

numbers = [2,4,6]
doubled_number = []
for num in numbers:
    doubled_number.append(num*2)

print(doubled_number)

# With list comprehension:
numbers = [1,2,3,4]
tenx_even_numbers = [num*10 for num in numbers if num<4]
print(tenx_even_numbers)

numbers = range(1,10)
result = [num if num%2==0 else 'odd' for num in numbers]
print(result)

#nested list comprehension
matrix = [[1,2,3],[4,5,6],[7,8,9]]
resulted_numbers = [num for row in matrix for num in row]
print(resulted_numbers)