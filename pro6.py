from random import randint as ri

UserX = str(input("как жизнь блатная?: "))

def kay (a,b,c):
    result = {a:ri(b,c+1)}
    return result

print (kay(UserX,10,20))
