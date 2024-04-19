print("Hello! Welcome to Number Analyzer")
user_input = input("Enter a series of numbers separated by spaces: ")
numbers = [int(num) for num in user_input.split()]
sum = 0
avg = 0
largest_num = numbers[0]
smallest_num = numbers[0]
index = 1

#for loop
for number in numbers:
    #sum
    sum += number
    #average
    if len(numbers) > 0:
        avg = sum/len(numbers)
    else:
        avg = 0

#while loop
while index < len(numbers):
    current_num = numbers[index]
    #largest num
    if current_num > largest_num:
        largest_num = current_num
    
    #smallest num
    if current_num < smallest_num:
        smallest_num = current_num
    
    index += 1

print("Sum: " + str(sum))
print("Average: " + str(avg))
print("Largest number: " + str(largest_num))
print("Smallest number: " + str(smallest_num))

