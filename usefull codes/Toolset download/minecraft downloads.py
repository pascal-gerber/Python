import webbrowser

clicker = input("do you want to download an autoclicker? y/n:")
xray = input("do you want to download a minecraft xray texturepack? y/n:")
impact = input("do you want to download impact? y/n:")


if clicker == "y" :
    webbrowser.open('https://cdn.discordapp.com/attachments/609992457534570539/737037498588594196/AutoClicker.exe', new = 2)
if xray == "y" :
    webbrowser.open('https://cdn.discordapp.com/attachments/609992457534570539/737037780143702066/Xray_Ultimate_1.16_v3.4.0.zip', new = 2)
if impact == "y" :
    webbrowser.open('https://cdn.discordapp.com/attachments/609992457534570539/737018493983129800/installer-0.5.5.exe', new = 2)
    webbrowser.open('https://cdn.discordapp.com/attachments/609992457534570539/737018523506835552/ImpactInstaller-0.9.0.exe', new = 2)
    optifine = input("which version do you want to download(for optifine), 1.12, 1.12.2, 1.14.4, 1.16.1 :")

if optifine == "1.12":
    webbrowser.open('https://cdn.discordapp.com/attachments/609992457534570539/744956638858969088/OptiFine_1.12_HD_U_F5.jar', new = 2)
elif optifine == "1.12.2":
    webbrowser.open('https://cdn.discordapp.com/attachments/609992457534570539/744956646031360071/OptiFine_1.12.2_HD_U_F5.jar', new = 2)
elif optifine == "1.14.4":
    webbrowser.open('https://cdn.discordapp.com/attachments/609992457534570539/744956649168437328/OptiFine_1.14.4_HD_U_F5.jar', new = 2)        
elif optifine == "1.16.1":
    webbrowser.open('https://cdn.discordapp.com/attachments/609992457534570539/744956651764842586/OptiFine_1.16.1_HD_U_G2.jar', new = 2)        

#webbrowser.open(' ', new = 2)
    
