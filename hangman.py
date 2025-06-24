import random
word_list = ['apple', 'grape', 'mango', 'peach', 'lemon']
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = ['_'] * word_length
guessed_letters = []
lives = 6
print("🎮 Welcome to Hangman!")
print("Guess the fruit name:")
print(" ".join(display))
while lives > 0 and '_' in display:
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
        print("✅ Correct!")
    else:
        lives -= 1
        print(f"❌ Wrong! You have {lives} lives left.")

    print("Current Word: ", " ".join(display))
    print("-" * 30)
if '_' not in display:
    print("🎉 You won! The word was:", chosen_word)
else:
    print("💀 You lost! The word was:", chosen_word)