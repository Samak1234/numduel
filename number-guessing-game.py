import random # Built-in module used to generate random numbers

# Generate a random number between 1 and 100 (this is the secret answer)
secret = random.randint(1,100)

# Ask the user to guess the number and convert input to integer
guess = int(input("Guessa number between 1 and 100: "))


# Compare user's guess with the secret number
if guess == secret:
    print("Congratulations,Correct") # User guessed correctly
elif guess < secret:
    print("Guess Higher number") # Hint: number is bigger
else:
    print("Guess lower number")  # Hint: number is smaller