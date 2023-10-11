num = input("numero: ")
count = 0
total = 0
while num != '':
    count += 1
    num = float(num)
    total += num
    num = input("numero: ")

media = total/count

print(media)

