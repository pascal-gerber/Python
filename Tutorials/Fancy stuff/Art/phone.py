import time

e = input("off or on? : ")

def battery(f):
    if f == 1:
        print("")
    elif f == 2:
        print("")
    elif f == 3:
        print("")
    elif f == 4:
        print("")
    elif f == 5:
        print("")
    elif f == 6:
        print("")
    elif f == 7:
        print("")
    elif f == 8:
        print("")
    elif f == 9:
        print("")
    elif f == 10:
        print("")
    elif f == 11:
        print("")

if e == "on":
    r = 1
    while r != 12:
        battery(r)
        r += 1
        time.sleep(1)
    print("startup")
elif e == "off":
    r = 11
    while r != 0:
        battery(r)
        r -= 1
        time.sleep(1)
    print("shutdown")
else:
    print("This is a phone ")

