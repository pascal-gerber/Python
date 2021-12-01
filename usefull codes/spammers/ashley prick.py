import time
import keyboard

text = ["We're no strangers to love", "You know the rules and so do I", "A full commitment's what I'm thinking of", "You wouldn't get this from any other guy", "I just wanna tell you how I'm feeling", "Gotta make you understand", "Never gonna give you up", "Never gonna let you down", "Never gonna run around and desert you", "Never gonna make you cry", "Never gonna say goodbye", "Never gonna tell a lie and hurt you", "We've known each other for so long", "Your heart's been aching, but", "You're too shy to say it", "Inside, we both know what's been going on", "We know the game and we're gonna play it", "And if you ask me how I'm feeling", "Don't tell me you're too blind to see", "Never gonna give you up", "Never gonna let you down", "Never gonna run around and desert you", "Never gonna make you cry", "Never gonna say goodbye", "Never gonna tell a lie and hurt you", "Never gonna give you up", "Never gonna let you down", "Never gonna run around and desert you", "Never gonna make you cry", "Never gonna say goodbye", "Never gonna tell a lie and hurt you", "(Ooh, give you up)", "(Ooh, give you up)", "Never gonna give, never gonna give", "(Give you up)", "Never gonna give, never gonna give", "(Give you up)", "We've known each other for so long", "Your heart's been aching, but", "You're too shy to say it", "Inside, we both know what's been going on", "We know the game and we're gonna play it", "I just wanna tell you how I'm feeling", "Gotta make you understand", "Never gonna give you up", "Never gonna let you down", "Never gonna run around and desert you", "Never gonna make you cry", "Never gonna say goodbye", "Never gonna tell a lie and hurt you", "Never gonna give you up", "Never gonna let you down", "Never gonna run around and desert you", "Never gonna make you cry", "Never gonna say goodbye", "Never gonna tell a lie and hurt you", "Never gonna give you up", "Never gonna let you down", "Never gonna run around and desert you", "Never gonna make you cry", "Never gonna say goodbye", "Never gonna tell a lie and hurt you"]

time.sleep(1)
for i in text:
    
    i = i.replace("Never", "Always")
    i = i.replace("wouldn't", "whould")
    i = i.replace("Don't", "")
    i = i.replace("just", "don't")
    i = i.replace("heart", "head")
    i = i.replace("long", "short")
    i = i.replace("full", "fake")
    i = i.replace("shy", "stupid")
    i = i.replace(" no ", " ")

    keyboard.wait('Delete')
    keyboard.write(i)
    time.sleep(0.1)
    keyboard.press("Enter")
    time.sleep(0.1)
    keyboard.release("Enter")
