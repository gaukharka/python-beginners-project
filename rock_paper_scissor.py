import random
lists = {
    'r': '🪨',
    's': '✂️',
    'p': '📜'
}

count = 0

def rock_paper_scissor(user_input, computers_choice):
        print(f'You chose {lists[user_input]}')
        print(f'Computer chose {lists[computers_choice]}')

        if (user_input == 's' and computers_choice == 'r') or (
                user_input == 'p' and computers_choice == 's') or (
                user_input == 'r' and computers_choice == 'p'):
            print('You loose')
        elif (user_input == 'r' and computers_choice == 's') or (
                user_input == 's' and computers_choice == 'p') or (
                user_input == 'p' and computers_choice == 'r'):
            print('You won')
        else:
            print('Draw!')


while True:
    if count < 2:
        random_int = random.randint(0, 2)
        arr = ['r', 'p', 's']

        computers_choice = arr[random_int]
        user_input = input('Rock, paper or scissors? (r/p/s)')
        if user_input != 'r' and user_input != 'p' and user_input != 's':
            print('Invalid choice!')
        else:
            count += 1
            rock_paper_scissor(user_input, computers_choice)
    else:
        yes_no = input('Continue? (y/n)')
        if yes_no == 'y':
            count = 0
        elif yes_no == 'n':
            break
        else:
            print("Please, enter y or n!")

