# Me: https://github.com/ashkanch

from random import randint

def condition(guess, real_number,):
    
    if guess<real_number:
        print('the real number is more than your guess')
        return False
    elif guess>real_number:
        print('the real number is lower than your guess')
        return False
    
    elif guess == real_number:
        print('your guess is right!')
        return True

def guessing(n):
    i = 1
    while i<n:
        g = int(input('Enter your guess:    '))
        status = condition(g,correct)
        if status == False:
            i+=1
        if status == True:
            print("you won! \n \n")
            break
    else:
        print("you lost! \nBut I think you'll be better next time :)")


while True:

    correct = randint(0,100)
    print('\nWelcome to the Number Guessing Game! \nIm thinking of a number between 1 and 100.\n')    
    print('Select the difficality level \n 1. Easy(10 choises) \n 2. Medium(5 choices) \n 3. Hard(3 choices) \n 4. Exit')
    
    try:
        inp = int(input('Enter your choice:  '))
    except ValueError:
        print('Please enter a valid number')
    
    if inp == 4:
        break

    if inp == 1:
        guessing(11)

    elif inp == 2:
            guessing(6)
            
    elif inp == 3:
            guessing(4)



# https://roadmap.sh/projects/number-guessing-game