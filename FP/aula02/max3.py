x1 = float(input("number? "))
x2 = float(input("number? "))
x3 = float(input("number? "))
x4 = float(input("number? "))

mx = x1

if x2 > mx:
    mx = x2

elif x3 > mx:
    mx = x3

print("O máximo valor foi {}".format(mx))