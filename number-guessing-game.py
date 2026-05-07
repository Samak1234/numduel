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

limit_replay=0
while True:
    
    if limit_replay>=3:
        print("Number of replays Exhausted")
        break
    print("choose difficulty 1.Easy 2.Medium 3.Tough")
    difficulty=int(input("Choose difficulty level"))
    if difficulty==1:
        secret = random.randint(1,50)
        max_attempts=20
    elif difficulty==2:
        secret = random.randint(1,100)
        max_attempts=10
    else:
         secret=random.randint(1,500)
         max_attempts=7
    
    
    # Counter to track how many attempts the user makes
    no_of_attempts=0
    
    while True:
        
        
        print(f"remaining no of attempts are as follow,{max_attempts-no_of_attempts}")
        
        if no_of_attempts>=max_attempts:
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
        limit_replay+=1
        continue
    else:
        print("Thanks for playing, bye!")
        break