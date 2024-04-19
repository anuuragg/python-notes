print('Hello! Welcome to Grade Calculator!')
marks = int(input("Enter your marks: "))
if(marks <= 100):
    if(marks >= 90):
        print("A\nExcellent Work!")
    elif(marks >= 80):
        print("B\nGood Job!")
    elif(marks >= 70):
        print("C\nYou passed.")
    elif(marks >= 60):
        print("D\nYou passed, but consider studying more.")
    else:
        print("F\nYou failed. Please study harder.")
else:
    print("Invalid grade! Please enter a grade between 0 and 100.")