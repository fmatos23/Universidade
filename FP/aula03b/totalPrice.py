i1 = int(input("age 1: "))
i2 = int(input("age 2: "))
i3 = int(input("age 3: "))
i4 = int(input("age 4: "))

price1 = 0
price2 = 0
price3 = 0
price4 = 0


if i1 < 6:
    price1 = 0
elif i1 <= 12:
    price1 = 2.5
elif i1 <= 65:
    price1 = 5
elif i1 > 65:
    price1 = 2.5

if i2 < 6:
    price2 = 0
elif i2 <= 12:
    price2 = 2.5
elif i2 <= 65:
    price2 = 5
elif i2 > 65:
    price2 = 2.5

if i3 < 6:
    price3 = 0
elif i3 <= 12:
    price3 = 2.5
elif i3 <= 65:
    price3 = 5
elif i3 > 65:
    price3 = 2.5

if i4 < 6:
    price4 = 0
elif i4 <= 12:
    price4 = 2.5
elif 13 <= i4 <= 65:
    price4 = 5
elif i4 > 65:
    price4 = 2.5

total = price1 + price2 + price3 + price4
print(total)