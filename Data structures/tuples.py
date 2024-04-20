#Definie the tuple
fruits = ("apple", "banana", "cherry", "date", "elderberry")

#Accesing the first element
print("First element of the tuple fruits: ", fruits[0])
#Accessing the last element
print("Last element of the tuple fruits: ", fruits[-1])

#Slicing
sliced_fruits = fruits[1:3]
print(sliced_fruits)

#Length function
print(len(fruits))

#Updating tuple
fruits_list = list(fruits)
fruits_list.append("fig")
updated_fruits = tuple(fruits_list)
print(updated_fruits)

#Deleting elements
fruits_list = list(updated_fruits)
fruits_list.pop(3)
final_fruits = tuple(fruits_list)
print(final_fruits)

#Concatination of tuple
numbers = 1, 2, 3, 4, 5
fruits_and_numbers = final_fruits + numbers
print(fruits_and_numbers)

#Built in tuple functions
#count()
print (final_fruits.count("banana"))
#max()
print(max(numbers))
#min()
print(min(numbers))

#Deleting tuple
del numbers
#print(numbers)