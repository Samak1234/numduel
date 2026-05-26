"""
Number Guessing Game

- Generates a random number based on difficulty level
- Easy: 1-50 (20 attempts), Medium: 1-100 (10 attempts), Hard: 1-500 (7 attempts)
- User keeps guessing until correct or attempts exhausted
- Provides hints (higher/lower) and even/odd hint after halfway
- Tracks number of attempts and remaining attempts
- Stores and displays guess history using lists
- Score system with penalty per wrong guess
- Tracks best attempt across all games in session
- Option to replay after each game (max 3 replays)
- Quit option available during guessing
"""

from difficulty import choose_difficulty 
from hints import show_hint
import random  # Built-in module used to generate random numbers

best_attempt = float('inf')
limit_replay = 0

while True:

    hint_shown = False
 
    if limit_replay >= 3:
        print("Number of replays Exhausted")
        break
    print("\nChoose difficulty:")
    print("easy")
    print("medium")
    print("hard")

    difficulty = input("Choose difficulty level: ").lower()

    upper_limit, max_attempts, score = choose_difficulty(difficulty)

    if upper_limit is None:
        print("Please choose easy, medium, or hard!")
        continue


    # Secret number generated after difficulty selection
    secret = random.randint(1, upper_limit)

    # Counter to track how many attempts the user makes
    no_of_attempts = 0

    # List used to store all valid guesses
    guesses = []

    while True:

        print(f"\nRemaining no of attempts are as follow: {max_attempts - no_of_attempts}")

        if no_of_attempts >= max_attempts:
            print("Attempts Exhausted better luck next time")
            print(f"The secret number was: {secret}")

            # Show guess history after losing
            print(f"Your guesses were: {guesses}")

            break  # stop the game

        try:

            # Ask the user to guess the number
            guess_input = input(
                f"Guess a number between 1 and {upper_limit} "
                f"(or type quit): "
            ).lower()
            
            # Exit option for user
            if guess_input in ["quit", "exit", "q"]:
                print("You exited the game")

                # Show guesses before exiting
                print(f"Your guesses were: {guesses}")

                break

            # Convert input to integer after validation
            guess = int(guess_input)
                
            # Check if guess is within valid range
            if guess < 1 or guess > upper_limit:
                print("The number you entered is Out of Range")
                continue

        except ValueError:
            print("Please enter a whole number!")
            continue  # skip to next iteration
        
        # Increment attempt count after each guess
        no_of_attempts += 1
        
        # Store valid guesses inside list
        guesses.append(guess)

        # Show guess history
        print(f"Previous guesses: {guesses}")

        # Hint system after half attempts are used
        hint_shown = show_hint(
            secret,
            no_of_attempts,
            max_attempts,
            hint_shown
        )
        # Check if the guess matches the secret number
        if guess == secret:

            print("Ps you got it, Congratulations it's Correct Man")  # User guessed correctly
            print(f"You got it in {no_of_attempts} attempts")

            # Show guess history after winning
            print(f"Your guesses were: {guesses}")

            # Store best attempt score
            if no_of_attempts < best_attempt:
                best_attempt = no_of_attempts

            print(f"So far your best score is: {best_attempt}")

            break  # exits the loop

        elif guess < secret:
            print("Guess Higher number")  # Hint: number is bigger
            score-=10
        else:
            print("Guess lower number")  # Hint: number is smaller
            score-=10
        if score < 0:
            score = 0
    
    replay = input("\nDo you want to play again? ").lower()

    if replay == "yes":
        limit_replay += 1
        continue

    else:
        print("Thanks for playing, bye!")
        print(f"Game Over. Final Score: {score}")
        if best_attempt != float('inf'):
            print(f"Your best score this session: {best_attempt} attempts")

        break