a1, b1, a2, b2 = map(int, input().split())

if a1 == a2 and b1 == b2:
    print("= , [" + str(a1) + "," + str(b1) + "]")
elif a1 >= a2 and b1 <= b2:
    print("1 , [" + str(a1) + "," + str(b1) + "]")
elif a2 >= a1 and b2 <= b1:
    print("2 , [" + str(a2) + "," + str(b2) + "]")
else:
    x = max(a1, a2)
    y = min(b1, b2)
    if x > y:
        print("? , []")
    else:
        print("? , [" + str(x) + "," + str(y) + "]")
