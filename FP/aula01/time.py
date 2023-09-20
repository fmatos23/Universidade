segundos = int(input("tempo em segundos: "))

s = segundos % 60
m = segundos // 60 % 60
h = segundos // 3600

print("{:02d}:{:02d}:{:02d}".format(h, m, s))