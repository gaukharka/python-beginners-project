import random
def roll_dice(input_letter):
    if input_letter == 'y':
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        print(f"({x}, {y})")
    else:
        print('Invalid letter')

while True:
    input_letter = input('Roll the dice? (y/n)').lower()
    if input_letter == 'n':
        print('Thanks for playing!')
        break
    else:
        roll_dice(input_letter)
