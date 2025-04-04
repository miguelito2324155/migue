temperatura = int(input())

if temperatura > 30:
    print("it's hot")
elif temperatura < 10:
    print("it's cold")
else:
    print("it's ok")

if temperatura >= 100:
    print("water would boil")
elif temperatura <= 0:
    print("water would freeze")