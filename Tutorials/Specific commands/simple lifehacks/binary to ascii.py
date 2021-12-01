while 1:
    a = input("Binary code : ")
    total = 0

    for i in range(len(a)):
        if a[i] == "1":
            total += 2**i

    print(total)
