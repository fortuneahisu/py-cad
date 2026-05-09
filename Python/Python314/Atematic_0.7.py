"""
Relationship between functions
Hospital game
"""
import time
from random import randint
print('_' * 20)
print('Hospital game')
print('_' * 20)


def hospital_game():
    """Classic input-output code"""
    name = input('Input your first name and last name? ')
    age = input('How old are you? ')
    is_patient = input('Have you been here before?(True or False) ').title()
    while True:
        if is_patient == 'True':
            print('You can visit your assigned doctor.')
            time.sleep(2)
            print('You\'re with your doctor')
            time.sleep(5)
            print('You have cancer')
            time.sleep(2)
            print('You can: ')
            gameplay(name)
            break
        if is_patient == 'False':
            print('You have to register first')
            print(f'Name = {name}')
            print(f'Age = {age}')
            input('Input your acc number = ')
            is_patient = 'True'
            continue
        print('Input true or false')
        continue


def gameplay(name):
    """Gameplay of the hospital game"""
    survival_rate = randint(1, 100)
    print('1. Commit suicide\n'
          '2. Treat it\n'
          '3. Call your wife\n'
          '4. Ask questions')
    choice = int(input(f'What do you do {name.title()}? '))
    if choice == 1:
        time.sleep(1)
        print('You are dead')
    elif choice == 2:
        print('You\'re doctor is trying to save your life...')
        time.sleep(1)
        print('Treating...')
        time.sleep(2)
        if survival_rate >= 50:
            print('You survive cancer, you live on 😊😊🥳')
        else:
            print('You are dead 💀☠️😵')
        time.sleep(5)

    elif choice == 3:
        print('Calling wife...')
        time.sleep(2)
        print('She\'s not around, leave a typed note...')
        time.sleep(1)
        input('Say something to your wife...')
        time.sleep(1)
        print('Sending...')
        time.sleep(1)
        print('Sent')
        time.sleep(1)
        print('You can: ')
        gameplay(name)
    elif choice == 4:
        input('Message: ')
        print('We\'ll see what we can do about it')
        time.sleep(2)
        gameplay(name)
    else:
        print('Invalid response')


hospital_game()
