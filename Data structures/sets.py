#Defining set
fruits = {'apple', 'banana', 'orange', 'grape'}
print(fruits)

#accesing & deleting values
is_banana_in_fruits = 'banana' in fruits
print(is_banana_in_fruits)

fruits.remove('orange')
print(fruits)

#Updating set
more_fruits = {'mango', 'pineapple', 'apple'}
fruits.update(more_fruits)
print(fruits)

#Basic set operations
citrus_fruits = {'orange', 'lemon', 'lime'}
#union
union = fruits | citrus_fruits #OR union = fruis.union(citrus_fruits)
print(union)
#intersection
intersection = fruits & citrus_fruits #OR intersection = fruits.intersection(citrus_fruits)
print(intersection)
#difference 
difference  = fruits - citrus_fruits #OR difference = fruits.deifference(citrus_fruits)
print(difference )

#Built-in set functions
#length()
print(len(fruits))
#issubset()
print(fruits.issubset(citrus_fruits))
#isdisjoint()
print(fruits.isdisjoint(citrus_fruits))