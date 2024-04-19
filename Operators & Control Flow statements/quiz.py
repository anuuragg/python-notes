print("Hello! Welcome to the Quiz Game!")
score = 0

print('\n1. Who wrote the novel "Pride and Prejudice"?')
print("a. Jane Austen")
print("b. Charlotte Brontë")
print("c. Charles Dickens")
print("d. George Eliot")

ans = input("select your answer(a, b, c, d): ")
if(ans == "a"):
    score += 1
elif(score != 0):
    score -= 1

print('\n2. Which famous play begins with the line "To be, or not to be"?')
print("a. Othello")
print("b. Macbeth")
print("c. Hamlet")
print("d. King Lear")

ans = input("select your answer(a, b, c, d): ")
if(ans == "c"):
    score += 1
elif(score != 0):
    score -= 1

print('\n3. Which of these works is a play written by Oscar Wilde?')
print("a. Great Expectations")
print("b. The Importance of Being Earnest")
print("c. A Tale of Two Cities")
print("d. Wuthering Heights")

ans = input("select your answer(a, b, c, d): ")
if(ans == "b"):
    score += 1
elif(score != 0):
    score -= 1

    
print("\nYour Score is "+ str(score))
