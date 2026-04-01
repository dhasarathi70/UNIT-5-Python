import random

words_dict = {
    "python": "Programming language",
    "banana": "A yellow fruit",
    "computer": "Electronic device",
    "security": "Protection from threats",
    "hangman": "This game itself"
}

while True:
    words_list = list(words_dict.keys())
    word = random.choice(words_list)
    hint = words_dict[word]

    guesses = []
    mistakes = 0
    max_attempts = 6
    hint_used = False
    first_turn = True

    print("\nWelcome to Hangman!")

    while mistakes < max_attempts:
        display_word = ""

        for letter in word:
            if letter in guesses:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word.strip())
        print("Wrong guesses left:", max_attempts - mistakes)
        print("Guessed letters:", ", ".join(guesses))

        if all(letter in guesses for letter in word):
            print("You won! The word was:", word)
            break

        if first_turn:
            print("\n1 = Guess | 2 = Hint | 3 = Show Possible Words")
            choice = input("Choice: ")

            if choice == "1":
                guess = input("Enter a letter: ").lower()

            elif choice == "2":
                if not hint_used:
                    print("Hint:", hint)
                    mistakes += 1
                    hint_used = True
                else:
                    print("Hint already used!")
                continue

            elif choice == "3":
                print("\nPossible words:")
                possible_words = []

                for w in words_list:
                    if len(w) != len(word):
                        continue

                    match = True
                    for i in range(len(word)):
                        if word[i] in guesses:
                            if w[i] != word[i]:
                                match = False
                                break
                        else:
                            if w[i] in guesses:
                                match = False
                                break

                    if match:
                        possible_words.append(w)

                print(possible_words)
                continue

            else:
                print("Invalid choice")
                continue

            first_turn = False

        else:
            guess = input("Enter next letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter a valid single letter.")
            continue

        if guess in guesses:
            print("Already guessed.")
            continue

        guesses.append(guess)

        if guess in word:
            print("Correct!")
        else:
            print("Wrong!")
            mistakes += 1

        if mistakes == max_attempts:
            print("You lost! The word was:", word)

    print("Game Over")

    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing!")
        break
