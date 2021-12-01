import random
import keyboard
import pyperclip

text = ['ᒷ', '.', '╎', '↸', '!', '|', '⚍', 'ꖌ', ',', 'ᓭ', 'ꖎ', '⎓', 'ᔑ', 'ʖ', 'ᒲ', '¡', 'ᓵ', '⍑', 'ℸ', '𝙹', 'リ']

new = ""

while 1:
    new = ""
    keyboard.wait("Ctrl + V")
    for i in range(random.randint(10, 100)):
        new += random.choice(text)
    pyperclip.copy(new)

                                
