import random

# Predefined list of words
words = ["python", "apple", "table", "chair", "plant"]

# Choose a random word
word = random.choice(words)

# Create display with underscores
guessed_word = ["_"] * len(word)

# Track guessed letters
guessed_letters = []

# Limit incorrect guesses
incorrect_guesses = 0
max_attempts = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")

# Game loop
while incorrect_guesses < max_attempts and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Incorrect guesses left:", max_attempts - incorrect_guesses)
    print("Guessed letters:", guessed_letters)

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("✅ Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("❌ Wrong guess!")
        incorrect_guesses += 1

# Game result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)