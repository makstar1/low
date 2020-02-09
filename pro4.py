from random import randint as ri

a = int(input( "введите длину списка: "))
b = int(input("введите  максимальное значение элемента списка: "))

def listFunc (x,y):
    list = []
    for i in range(x):
        list.append(ri(0,y+1))
    return list

print(listFunc(a,b))
