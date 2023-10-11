num = int(input("num: "))
total = 0
for c in range(1, num):
    if num % c == 0:
        print(c)
        total += c

if total < num:
    print("numero deficiente")
elif total == num:
    print("numero perfeito")
elif total > 18:
    print("numero abundante")
