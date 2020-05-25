from Fireworks import *

print('Would you like to customize it？ (yes or no)')
f = input()
if f == 'yes':
    number = int(input('Number of particles in a firework:(Default 5)\n'))
    cs = []
    for i in range(5):

        cs.append(tuple([int(i) for i in input('Colors' + str(i) + ':(Default 2 of them are with single colors (red, green) '
                                                  'and the other 3 with randomly generated colors) (style:(1, 0, 0, 1)\n').split(',')]))
    print(cs)

else:
    number = 10
    cs = [(random.random(), random.random(), random.random(), 1), (1, 0, 0, 1),
          (random.random(), random.random(), random.random(), 1), (0, 1, 0, 1),
          (random.random(), random.random(), random.random(), 1)]

main(number, cs, f)
