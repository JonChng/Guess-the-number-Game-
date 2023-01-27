#Number Guessing Game Objectives:

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).                                                                            

import random

ans = random.randint(1,101)

mode = {"easy":10, "hard":5}

game = input("Please input the game mode you would like: 'easy' or 'hard': ")

lives = mode[game]

print(f"You now have {lives} tries to guess the number.")

while lives > 0:

  guess = int(input("Please input your guess: "))

  if guess > ans:
    print("Too high.")
    lives -= 1
    print(f"You now have {lives} lives remaining.")

  elif guess < ans:
    print("Too low")
    lives -= 1
    print(f"You now have {lives} lives remaining.")

  else:
    print(f"You win! The answer was {ans}.")
    break

if lives == 0:
  print(f"You lose. The answer was {ans}.")
    
