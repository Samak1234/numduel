"""
Number Guessing Game

- Generates a random number between 1 and 100
- User keeps guessing until correct
- Provides hints (higher/lower)
- Tracks number of attempts
"""
import random # Built-in module used to generate random numbers
print("choose difficulty")
print("1.Easy")
print("2.Medium")
print("3.Tough")
while True:
    # Generate a random number between 1 and 100 (this stays constant for one game)
    secret = random.randint(1,100)
    # Counter to track how many attempts the user makes
    no_of_attempts=0

    while True:
        if no_of_attempts>=2:
            print("Attempts Exhausted better luck next time")
            break #stop the game
        try:
            # Ask the user to guess the number and convert input to integer
            guess = int(input("Guess a number between 1 and 100: "))
        except:
            print("Please enter a whole number!")
            continue #skip to next iteration
        # Increment attempt count after each guess
        no_of_attempts+=1

        # Check if the guess matches the secret number
        if guess == secret:
            print("Ps you got it,Congratulations it's Correct Man") # User guessed correctly
            print(f"You got it in {no_of_attempts} attempts")
            break # exits the loop

        elif guess < secret:
            print("Guess Higher number") # Hint: number is bigger
        else:
            print("Guess lower number")  # Hint: number is smaller

    replay = input("Do you want to play again? ")
    if replay.lower() == "yes":
        continue
    else:
        print("Thanks for playing, bye!")
        break