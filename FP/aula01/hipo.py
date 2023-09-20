from math import *


catA = float(input("cateto A: "))
catB = float(input("cateto B: "))

hipo = sqrt((catA ** 2) + (catB ** 2))

angulo = degrees(acos(catA/hipo))

print("hipotenusa é {} e angulo entre o cateto A e a hipotenusa é {:.1f}".format(hipo, angulo))
