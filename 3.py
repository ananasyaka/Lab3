n=0
a= input('Введите слово ')
b="ф"
for i in a:
    if i == b:
        n=n+1
if n>0:
    print ("Ого! Это редкое слово!")
else:
    print ("Эх, это не очень редкое слово...")
