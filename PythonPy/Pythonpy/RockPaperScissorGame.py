from random import choice, randint, shuffle
from time import sleep

print('{:=^40}'.format( ' JO KEN PO '))
print('{:=^40}\n'.format( ' THE GAME '))
print('Sua Opcoes:')
print(' [ 0 ] ROCK')
print(' [ 1 ] PAPER')
print(' [ 2 ] SCISSOR')
user = ['ROCK', 'PAPER', 'SCISSOR']
play = int(input('YOUR PLAY?: '))
if play < 0 or play >= 3:
    print('\033[1;30;41mWRONG ENTRY. INSERT AN ENTRY BETWEEN 0 AND 2\033[m')
    exit()

nome = user[play]

print('{:*^20}'.format(' JO... '))
sleep(1)
print('{:*^20}'.format(' KEN... '))
sleep(1)
print('{:*^20}\n'.format(' PO !! '))

pc = ['ROCK', 'PAPER', 'SCISSOR']
chosen = pc.index(choice(pc))
name_pc = pc[chosen]

if chosen == play:
    msg = 'DRAW! TRY AGAIN'
elif (chosen == 0 and play == 2) or (chosen == 2and play == 1) or (chosen == 1\
        and play == 0):
    msg = 'COMPUTER WINS!! YOU \033[7;31mLOST\033[m :('
else:
    msg = 'YOU \033[7;30mWON\033[m !! CONGRATULATIONS!!'

print('-='*20)
print('Your Turn: \033[4;36m{}\033[m'.format(name))
print('*'*40)
print('Computer Turns: \033[4;33m{}\033[m'.format(name_pc))
print('-='*20)
print(msg)