from Fireworks import *


print('Would you like to customize it？ (yes or no)')
f = input()
if f == 'yes':
    number = input('Number of particles in a firework:(Default 100)\n')
    cs = input('Colors:(Default 2 of them are with single colors (red, green) '
               'and the other 3 with randomly generated colors) (style:(1, 0, 0, 1)\n')
else:
    number = 10
    cs = [(random.random(), random.random(), random.random(), 1), (1, 0, 0, 1),
          (random.random(), random.random(), random.random(), 1), (0, 1, 0, 1),
          (random.random(), random.random(), random.random(), 1)]

main(number, cs)