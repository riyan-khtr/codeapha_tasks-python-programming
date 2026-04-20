import random

# Hangman patterns (6 attempts → 0 attempts)
hangman_stages = [
"""
   -----
   |   |
       |
       |
       |
       |
=========
""",
"""
   -----
   |   |
   O   |
       |
       |
       |
=========
""",
"""
   -----
   |   |
   O   |
   |   |
       |
       |
=========
""",
"""
   -----
   |   |
   O   |
  /|   |
       |
       |
=========
""",
"""
   -----
   |   |
   O   |
  /|\  |
       |
       |
=========
""",
"""
   -----
   |   |
   O   |
  /|\  |
  /    |
       |
=========
""",
"""
   -----
   |   |
   O   |
  /|\  |
  / \  |
       |
=========
"""
]

words = ("apple", "kittens", "fish", "penguine", "women", "banana")

word = random.choice(words).lower()
guessed = ["_"] * len(word)

attempts = 6
guessed_letter = []

print("Welcome to Hangman Game")
print("Guess the word")
print(hangman_stages[0])
print(" ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("\nEnter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Only enter alphabet letters")
        continue

    if guess in guessed_letter:
        print("You've already guessed the letter:", guess)
        continue

    guessed_letter.append(guess)

    if guess in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

    # Show hangman drawing
    print(hangman_stages[6 - attempts])
    print(" ".join(guessed))

if "_" not in guessed:
    print("\nCongratulations! You win!")
    print("The word is:", word)
else:
    print("\n Game Over!")
    print(hangman_stages[6])
    print("The word was:", word)