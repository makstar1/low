from random import randint as ri

a = int(input ("введите длину первого списка: "))
b = int(input ("введите  максимальное значение элемента первого списка: "))
c = int(input ("введите длину второго списка: "))
d = int(input ("введите  максимальное значение элемента второго списка: "))

def listFunc2 (x,y,w,z):
    list1 = []
    for i in range(x):
        list1.append(ri(0, y+1))

    list2 = []
    for e in range(w):
        list2.append(ri(0, z+1))

    list3 =[]
    for s in list1:
        if s in list2:
            list3.append(s)

    if len(list3) == 0:
        print ("совпадений нет")
        return list32
    else:
        return list(set(list3))

print (listFunc2(a,b,c,d))