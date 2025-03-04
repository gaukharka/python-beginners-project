import random
def guess_number():
    guessed_number = random.randint(1,100)
    while True:
        try:
            user_input = input("Guess the number between 1 and 100: ")
            user_input = int(user_input)
            if user_input == guessed_number:
                print('Congratulation! You guessed the number!')
                break
            elif user_input >= guessed_number:
                print('Too high!')
            else:
                print('Too low!')
        except ValueError:
            print("Please, enter a valid number!")


guess_number()

