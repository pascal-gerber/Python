import re
#regex is imported as re

#it needs a pattern and a text
pattern = "[0-9]*[$]{1}"

text = "value in bank = 456744$"
################################################

#re findall is the most used but there are others
value = re.findall(pattern, text)
#it simply gives out the value it finds true to the pattern.

print(value)

################################################

#re.search tells you in which index it is.
index = re.search(pattern, text)

print(index)

#patterns can also be equiped with "or"/"and".
newPattern = ("(value|bank)")

words = re.findall(newPattern, text)

print(words)
