"""
NumDuel - Number Guessing Game

Features:
- Difficulty levels:
  - Easy: 1-50 (20 attempts)
  - Medium: 1-100 (10 attempts)
  - Hard: 1-500 (7 attempts)
- Random number generation based on selected difficulty
- Higher/lower guessing hints
- Additional even/odd and divisibility hints
- Guess history tracking
- Score system with penalties for incorrect guesses
- Best attempt tracking during current session
- Replay system (max 3 replays)
- Input validation
- Quit option during gameplay
- Modular architecture:
  - difficulty.py
  - hints.py
  - validators.py
  - scoring.py
  - replay.py
  - leaderboard.py
- JSON-based leaderboard persistence
- Leaderboard display across game sessions

Learning Focus:
- Functions and modules
- Separation of concerns
- Refactoring
- JSON persistence
- File handling
- Structured data
- Software architecture fundamentals
"""

from difficulty import choose_difficulty 
from hints import show_hint
from validators import is_valid_guess
from scoring import reducing_score
from replay import wants_replay
from leaderboard import save_score
from leaderboard import show_leaderboard
import random  # Built-in module used to generate random numbers

best_attempt = float('inf')
limit_replay = 0
player_name = input("Enter your name: ")
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
            if not is_valid_guess(guess, upper_limit):
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
            save_score(no_of_attempts)
            # Show guess history after winning
            print(f"Your guesses were: {guesses}")

            # Store best attempt score
            if no_of_attempts < best_attempt:
                best_attempt = no_of_attempts

            print(f"So far your best score is: {best_attempt}")

            break  # exits the loop

        elif guess < secret:
            print("Guess Higher number")  # Hint: number is bigger
            score = reducing_score(score)
        else:
            print("Guess lower number")  # Hint: number is smaller
            score = reducing_score(score)
        if score < 0:
            score = 0
    
    if wants_replay():
        limit_replay +=1
        continue

    else:
        print("Thanks for playing, bye!")
        print(f"Game Over. Final Score: {score}")
        if best_attempt != float('inf'):
            print(f"Your best score this session: {best_attempt} attempts")
            show_leaderboard()

        break