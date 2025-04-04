a1, b1, a2, b2 = map(int, input().split())
inicio = max(a1, a2)
fin = min(b1, b2)
if inicio > fin:
    print("[]")
else:
    print(f"[{inicio},{fin}]")
