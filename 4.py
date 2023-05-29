import random

n=0
i=0
while n < 3:
    a=random.randint(0,9)
    b=random.randint(0,9)
    print (a,"+",b,"=")
    c=int(input())
    s=a+b
    if c == s:
        i=i+1
        print ("Верно!")
    else:
        n=n+1
        print ("Не верно!")
print ("Игра окончена. Правильных ответов:", i)

