import mouse
import pyautogui
import keyboard
import time



#pyautogui.moveTo(100, 150)

#pyautogui.dragTo(100, 150)
#pyautogui.dragRel(0, 10)
#mouse.get_position()
#mouse.click('left')
#pyautogui.moveRel(500, 100)

def thirthpath(num):
    for i in range(num):
        mouse.move("3000", "1500")
        mouse.click("left")
        time.sleep(0.1)

def secondpath(num):
    for i in range(num):
        mouse.move("3000", "1300")
        mouse.click("left")
        time.sleep(0.1)

def firstpath(num):
    for i in range(num):
        mouse.move("3000", "1100")
        mouse.click("left")
        time.sleep(0.1)

def place(but):
    keyboard.press(but)
    time.sleep(0.1)
    keyboard.release(but)
    time.sleep(0.1)
    mouse.click("left")
    time.sleep(0.5)
    mouse.click("left")
    time.sleep(0.2)

def startgame():
    keyboard.press("space")
    time.sleep(0.1)
    keyboard.release("space")
    time.sleep(0.2)
    keyboard.press("space")
    time.sleep(0.1)
    keyboard.release("space")

def puttower(info):
    mouse.move(info[1], info[2])
    place(info[0])

def mousego(info):
    mouse.move(info[1], info[2])

def placeandupgrade(waittime, farm):
    global firstvillage
    puttower(farm)
    mousego(firstvillage)
    time.sleep(waittime)
    firstpath(2)
    mousego(firstvillage)

def upgradeFarm(farm):
    time.sleep(0.2)
    mousego(farm)
    time.sleep(0.1)
    mouse.click("left")
    time.sleep(0.1)
    firstpath(1)
    time.sleep(0.5)

def farm(taime):
    global firstfarm
    global thirtfarm
    global sixthfarm
    global eithfarm
    for i in range(taime):
        mousego(firstfarm)
        time.sleep(0.25)
        mousego(thirtfarm)
        time.sleep(0.25)
        mousego(sixthfarm)
        time.sleep(0.25)
        mousego(eithfarm)
        time.sleep(0.25)
    time.sleep(0.25)

def upgrade(monkey, path, amount):
    time.sleep(0.1)
    mousego(monkey)
    if path == 1:
        firstpath(amount)
    elif path == 2:
        secondpath(amount)
    elif path == 3:
        thirthpath(amount)
    time.sleep(0.1)

def continueGame():
    mouse.move("1900", "1800")
    mouse.click("left")
    time.sleep(2)
    mouse.move("2200", "1700")
    mouse.click("left")
    time.sleep(1)
    mouse.click("left")
    time.sleep(1)
    keyboard.press("Space")
    time.sleep(0.1)
    keyboard.release("Space")

firstdart = (["q", "1500", "940"])
seconddart =  (["q", "1630", "940"])
firstalch = (["f", "1550", "800"])
firstapprentice = (["a", "1400", "700"])

firstfarm = (["h", "780", "1950"])
secondfarm = (["h", "1104", "1950"])
thirtfarm  = (["h", "1428", "1950"])
fourthfarm =(["h", "780", "1626"])
fifthfarm =(["h", "1428", "1626"])
sixthfarm =(["h", "780", "1302"])
seventhfarm =(["h", "1104", "1302"])
eithfarm = (["h", "1428", "1302"])

firstvillage = (["k", "1104", "1626"])


keyboard.wait("1")
puttower(firstdart)
time.sleep(0.3)
thirthpath(3)
startgame()
time.sleep(20)
secondpath(2)
time.sleep(50)
puttower(firstfarm)
time.sleep(12.5)
firstpath(1)
mousego(firstvillage)
time.sleep(20)
firstpath(1)
mousego(firstvillage)
time.sleep(29)
puttower(secondfarm)
time.sleep(5)
for i in range(2):
    time.sleep(8)
    firstpath(1)
    mousego(firstvillage)
time.sleep(26)
puttower(firstalch)
firstpath(2)
puttower(seconddart)
thirthpath(3)
secondpath(2)
time.sleep(0.1)
mousego(firstvillage)
time.sleep(10)
placeandupgrade(10, thirtfarm)
farm(2)
placeandupgrade(10, fourthfarm)
farm(10)
placeandupgrade(5, fifthfarm)
farm(10)
placeandupgrade(1, sixthfarm)
farm(10)
placeandupgrade(1, seventhfarm)
farm(10)
placeandupgrade(1, eithfarm)
farm(12)
time.sleep(0.1)
firstpath(1)
farm(13)
placeandupgrade(0.1, firstapprentice)
firstpath(1)
thirthpath(2)
farm(13)
upgradeFarm(seventhfarm)
farm(9)
upgradeFarm(sixthfarm)
farm(11)
upgradeFarm(fifthfarm)
farm(9)
upgradeFarm(fourthfarm)
farm(13)
upgradeFarm(thirtfarm)
farm(10)
continueGame()
upgradeFarm(secondfarm)
farm(19)
upgrade(firstfarm, 1, 2)
farm(12)
upgrade(firstdart, 3, 1)
upgrade(seconddart, 3, 1)
farm(10)
upgradeFarm(secondfarm)
farm(20)
upgradeFarm(thirtfarm)
farm(20)
upgradeFarm(fourthfarm)
farm(20)
upgradeFarm(fifthfarm)
farm(20)
upgradeFarm(sixthfarm)
farm(20)
upgradeFarm(seventhfarm)
farm(20)
upgradeFarm(eithfarm)


firstpath(1)
farm(12)

puttower(firstvillage)
thirthpath(4)
farm(13)



"""
time.sleep(1)
puttower(seconddart)
mouse.move("1104", "1950")
"""




#keyboard.wait("1")
#mouse.move("780", "1950")
#mouse.move("1104", "1950")
#324










