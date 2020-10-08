from random import randint

n= int(randint(1,9))
p=0
t=0
while p != n:
    p = int(input('Your guess: '))
    t += 1
    if p == n:
        print('Correct! Score %i' % t)
    elif p< n:
        print('Insert a bigger number')
    else:
        print('Insert a small number')
print('Game Over')

########