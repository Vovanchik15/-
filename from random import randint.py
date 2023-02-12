from random import randint

game = True
num = randint(1,100)

file=open('game_result', 'w', encoding="utf8")

print('Попробуй угадай число от 1 до 100')
file.write('Попробуй угадай число от 1 до 100\n')
while game:
    guess = int(input('Ваше предположение: '))
    
    if guess == num:
        print('Вы угадали верно!')
        file.write('Вы угадали верно!\n')
        game = False
    elif guess<num:
        print(f'Число больше {guess}')
        file.write(f'Число больше {guess}\n')
    else:
        print(f'Число меньше {guess}')
        file.write(f'Число меньше {guess}\n')
        

file.close()









