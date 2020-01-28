from random import randint as ri

A = ri(0,10)
B = ri(0,10)
D = ri (0,10)

if A > B:
    print ("Юхууу")
elif A < B:
    print ("печалька")
elif A == B:
    print ("Теперь эта!")
    if (A + B) < D:
        print ("Юхууу")
    elif (A + B) > D:
        print ("печалька")
    elif (A + B) == D:
        print ("Страдания")