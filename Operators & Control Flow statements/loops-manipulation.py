import random

def number_guessing_game():
    target_number = random.randint(1, 100)
    print("Guess the number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))

        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.")
            continue  
        
        if guess == target_number:
            print("Congratulations! You guessed the correct number!")
            break 
        
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            pass  

    else:
        print(f"You couldn't guess the number. The correct number was {target_number}.")

number_guessing_game()
