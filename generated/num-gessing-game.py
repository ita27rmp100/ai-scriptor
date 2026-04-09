import random

def number_guessing_game():
    number_to_guess = random.randint(1, 10)
    guess = None
    attempts = 0

    while guess != number_to_guess:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low")
        elif guess > number_to_guess:
            print("Too high")
        else:
            print(f"Congratulations! You found the number in {attempts} attempts")

def main():
    play_again = "y"
    while play_again.lower() == "y":
        number_guessing_game()
        play_again = input("Would you like to play again? (y/n): ")
    print("Goodbye")

if __name__ == "__main__":
    main()
