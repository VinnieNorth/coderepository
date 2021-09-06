list = [1, 2, 3, 4, 5, 6, 7, 8, 9,"A", "B", "C", "D", "E", "F"]

while True:
    num = int(input())
    sum1 = 0
    sum2 = 0
    if num > 128:
        print("You're Number is bigger than 128, so we can't process it.")
        break

    if num >= 128:
        a = (1)
        num = num - 128
    else:
        a = (0)

    if num >= 64:
        b = (1)
        num = num - 64
    else:
        b = (0)

    if num >= 32:
        c = (1)
        num = num - 32
    else:
        c = (0)

    if num >= 16:
        d = (1)
        num = num - 16
    else:
        d = (0)

    if num >= 8:
        e = (1)
        num = num - 8
    else:
        e = (0)

    if num >= 4:
        f = (1)
        num = num - 4
    else:
        f = (0)

    if num >= 2:
        g = (1)
        num = num - 2
    else:
        g = (0)

    if num >= 1:
        h = (1)
        num = num - 1
    else:
        h = (0)

    print (a, b, c, d, e, f, g, h)

