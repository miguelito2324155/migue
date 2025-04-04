def min_banknotes_and_coins(euros, cents):
    denominations = [
        (50000, "Banknotes of 500 euros"),
        (20000, "Banknotes of 200 euros"),
        (10000, "Banknotes of 100 euros"),
        (5000, "Banknotes of 50 euros"),
        (2000, "Banknotes of 20 euros"),
        (1000, "Banknotes of 10 euros"),
        (500, "Banknotes of 5 euros"),
        (200, "Coins of 2 euros"),
        (100, "Coins of 1 euro"),
        (50, "Coins of 50 cents"),
        (20, "Coins of 20 cents"),
        (10, "Coins of 10 cents"),
        (5, "Coins of 5 cents"),
        (2, "Coins of 2 cents"),
        (1, "Coins of 1 cent")
    ]

    total_cents = euros * 100 + cents

    for value, label in denominations:
        count = total_cents // value
        total_cents %= value
        print(f"{label}: {count}")

e, c = map(int, input().split())
min_banknotes_and_coins(e, c)
