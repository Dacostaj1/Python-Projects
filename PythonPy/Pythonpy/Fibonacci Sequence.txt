Nant = 1
Fibonacci = 0

n = int(input('Insert Number:(Number of elements sequence) '))

while n != 0:
    print('{}'.format(Fibonacci), end=' → ')
    Fibonacci = Fibonacci + Nant
    Nant = Fibonacci - Nant
    n -= 1
print('END')
