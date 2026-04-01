import random

print("Welcome to Dice Game!")

while True:
    input("\nPress Enter to roll the dice...")

    user_roll = random.randint(1, 6)
    print("You rolled:", user_roll)

    cpu_roll = random.randint(1, 6)
    print("Computer rolled:", cpu_roll)

    if user_roll > cpu_roll:
        print("You win!")
    elif cpu_roll > user_roll:
        print("Computer wins!")
    else:
        print("It's a tie!")

    again = input("\nPlay again? (y/n): ").lower()

    if again != "y":
        print("Thanks for playing!")
        break
