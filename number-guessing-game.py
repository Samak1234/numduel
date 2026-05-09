"""
Number Guessing Game

- Generates a random number based on difficulty level
- Easy: 1-50 (20 attempts), Medium: 1-100 (10 attempts), Hard: 1-500 (7 attempts)
- User keeps guessing until correct or attempts exhausted
- Provides hints (higher/lower)
- Tracks number of attempts and remaining attempts
- Option to replay after each game
"""
import random # Built-in module used to generate random numbers

best_attempt = float('inf')
limit_replay = 0

while True:

    if limit_replay >= 3:
        print("Number of replays Exhausted")
        break

    print("choose difficulty 1.Easy 2.Medium 3.Tough")
    try:
        difficulty = int(input("Choose difficulty level: "))
        # Generate a random number based on difficulty (this stays constant for one game)
        if difficulty == 1:
            upper_limit = 50
            secret = random.randint(1, upper_limit)
            max_attempts = 20
        elif difficulty == 2:
            upper_limit = 100
            secret = random.randint(1, upper_limit)
            max_attempts = 10
        else:
            upper_limit = 500
            secret = random.randint(1, upper_limit)
            max_attempts = 7
    except:
        print("Please enter a valid number!")
        continue

    # Counter to track how many attempts the user makes
    no_of_attempts = 0

    while True:

        print(f"remaining no of attempts are as follow,{max_attempts - no_of_attempts}")

        if no_of_attempts >= max_attempts:
            print("Attempts Exhausted better luck next time")
            break #stop the game
        try:
            # Ask the user to guess the number and convert input to integer
            guess = int(input(f"Guess a number between 1 and {upper_limit} :"))
        except:
            print("Please enter a whole number!")
            continue #skip to next iteration

        # Increment attempt count after each guess
        no_of_attempts += 1

        # Check if the guess matches the secret number
        if guess == secret:
            print("Ps you got it,Congratulations it's Correct Man") # User guessed correctly
            print(f"You got it in {no_of_attempts} attempts")

            if no_of_attempts < best_attempt:
                best_attempt = no_of_attempts

            print(f"So far your best score is: {best_attempt}")
            break # exits the loop

        elif guess < secret:
            print("Guess Higher number") # Hint: number is bigger
        else:
            print("Guess lower number") # Hint: number is smaller

    replay = input("Do you want to play again? ")
    if replay.lower() == "yes":
        limit_replay += 1
        continue
    else:
        print("Thanks for playing, bye!")
        if best_attempt != float('inf'):
            print(f"Your best score this session: {best_attempt} attempts")
        break