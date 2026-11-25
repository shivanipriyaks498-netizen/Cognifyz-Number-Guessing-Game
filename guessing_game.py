
import random

print("================================")
print("   NUMBER GUESSING GAME")
print("================================")

secret_number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("Congratulations! You guessed correctly!")
elif guess < secret_number:
    print("Your guess is too low!")
else:
    print("Your guess is too high!")

print("The correct number was:", secret_number)
print("Thank you for playing!")
