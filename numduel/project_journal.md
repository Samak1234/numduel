NumDuel —> First Commit: Initial Implementation

This commit marks the beginning of NumDuel as a simple Python number-guessing game.

What I implemented:
- Imported Python's random module to generate a secret number.
- Used random.randint(1, 100) to generate a number between 1 and 100.
- Accepted a guess from the player using input().
- Converted the input into an integer using int().
- Used conditional statements (if, elif, else) to check whether the guess was correct, too low, or too high.


What I learned:

- Basic Python syntax and control flow.
- Generating random numbers.
- Taking user input and converting data types.
- Using conditional logic to make decisions.
Limitations of this version:

# - The player could make only one guess.
- There was no input validation, attempt tracking, scoring, or replay functionality.
- All game logic was written in a single Python file.
Why this commit matters:

This was the foundation of NumDuel. Later commits expanded the game with additional features and improved its architecture.