def formula (num):
    print(99 % 17)
    for i in range (0, 10):
        val = (num % 11 + i * (5 - num % 5)) % 11
        print(val)


formula(41)