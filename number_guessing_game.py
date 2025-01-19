
import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            if user_guess == number_to_guess:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
            elif user_guess < number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
    print("Thanks for playing!")

if __name__ == "__main__":
    number_guessing_game()
