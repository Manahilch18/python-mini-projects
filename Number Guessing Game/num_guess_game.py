import random
while True:
    secret_number = random.randint(1, 50)
    attempts = 0
    max_attempts = 5
    print("\nWelcome to Number Guessing Game")
    print("Guess a number between 1 and 50")
    print(f"You have {max_attempts} attempts.\n")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < secret_number:
                print("Too low, try again")
            elif guess > secret_number:
                print("Too high, try again")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                # Points based on attempts
                points = (max_attempts - attempts + 1) * 20
                print(f"Attempts used: {attempts}")
                print(f"🏆 Your score: {points} points")
                break
        except ValueError:
            print("❌ Please enter a valid number.")

    else:
        print("\n😢 Game Over!")
        print(f"The correct number was {secret_number}")
    # Play again option
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()

    if play_again == "yes":
        continue
    elif play_again == "no":
        print("👋 Thanks for playing!")
        break
    else:
        print("❌ Invalid input. Exiting game.")
        break
    