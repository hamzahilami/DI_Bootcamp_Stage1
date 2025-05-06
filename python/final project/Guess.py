import random

def number_guessing_game():
    random_number = random.randint(1, 100)
    max_attempts = 7

    for attempt in range(max_attempts):
        try:
            guess = int(input(f"Attempt {attempt + 1}: Guess a number between 1 and 100: "))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {random_number} in {attempt + 1} attempts.")
            break

    else:
        print(f"You ran out of attempts. The number was {random_number}.")

number_guessing_game()
