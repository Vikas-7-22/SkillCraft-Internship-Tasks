import random



def number_guessing_game():

    # Generate a random number between 1 and 100

    secret_number = random.randint(1, 100)

    print("🎯 Welcome to the Number Guessing Game!")

    print("I have picked a number between 1 and 100. Can you guess it?")



    while True:

        try:

            guess = int(input("Enter your guess: "))



            if guess < secret_number:

                print("Too low! Try again.")

            elif guess > secret_number:

                print("Too high! Try again.")

            else:

                print("🎉 Correct! You guessed the number!")

                break

        except ValueError:

            print("⚠ Please enter a valid number.")



# Run the game

number_guessing_game()