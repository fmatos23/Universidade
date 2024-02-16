soma = lambda x, y : x+y

def soma2(x,y):
    return x + y

print(soma(1,2))
print(soma2(1,2))

list = [2,3,4,6,3,0,1]
mytuple = (1,5,2,3)



student_tuples = [('André' , 'F' , 15), ('Filipe' , 'B', 16), ('Carolina', 'C', 19)]


print(sorted(list))
print(sorted(student_tuples , key=lambda student : student[0]))
