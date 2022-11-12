import random
import hangman_art
from hangman_words import word_list

chosen_word = random.choice(word_list)
display = []
guessed_letters = []
game_over = False
lives = 6

print(f'{hangman_art.logo}' + "\n\n\n")

for letter in chosen_word:
  display += "_"
print(f"{' '.join(display)}\n")
print(f"The word has {len(display)} letters. What is your guess?\n")

while not game_over:
    guess = input("\nPick a letter: ").lower()
   
    for position in range (len(chosen_word)):
      letter = chosen_word[position]
      if letter == guess:
        display[position] = letter
    print(f"{' '.join(display)}")
    
    if guess not in chosen_word:
      if guess in guessed_letters:
          print(f"\nYou've already selected the letter {guess} before. Try again\n")
          print(f"{' '.join(display)}")
      else:  
          lives -= 1
          stage = lives + 1
          guessed_letters += guess
          print (f"\nThe letter {guess} is not in the chosen word. Better luck next time. Lives remining {stage}")
          print (hangman_art.stages[stage])
          print(f"{' '.join(display)}")
    
    if "_" not in display or lives < 0:
        game_over = True
        if "_" not in display:
              print("\nYou Win")
        else:
              print("\nYou Lose")
