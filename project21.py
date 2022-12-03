from random import randint
from math import floor
num = int(input("How many pieces the cake should have: "))
print("1. Equal sizes\n 2. Any sizes\n 3. No two pieces with equal size")
size = int(input("Enter the index of your requirement: "))
if size == 1:
    angle = 360 / num
    print("Angle of each piece is {} degrees".format(angle))
elif size == 2:
    angles = [0 for i in range(num)]
    for i in range(360):
        angles[randint(0, num - 1)] += 1
    print("Angles are:")
    for i in range(1, num + 1):
        print("Piece {}: {} degrees".format(i, angles[i - 1]))
elif size == 3:
    dic = {}
    dic['a'] = randint(0, floor(360 / num))
    dic['d'] = ((720 / num) - (2 * dic['a'])) / (num - 1)
    print("Angles are:")
    for i in range(num):
        print("Piece {}: {} degrees".format(i + 1, dic['a'] + (i * dic['d'])))
else:
    print("Enter a valid input")
