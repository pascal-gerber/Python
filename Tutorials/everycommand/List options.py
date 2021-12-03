List = ["i", "am", "a", "sentance"]

#we can check if something is in a list trought
#multiple ways. The easiest is like that
if "am" in List:
    print("'am' is in the list\n")
#\n in a string will go to the next line (like the enter button)

#of course this also applies for strings
String = "i am a sentance"

if "am" in String:
    print("'am' is in the string\n")

#there are other options in the lists like sorting and selection specific

unsortedlist = [53, 1, 432, 52, 21, 12, 14.23, 53.23]
#this is a list of numbers ready to be sorted

unsortedlist.sort()
#sorts the list

print(unsortedlist)

#of course sort works also only for words

todolist = ["clean", "cook", "eat", "buy", "purchase drink"]

todolist.sort()
#same command

print(todolist)
print("both sorted!\n")

#Note: String and number list cannot be Sorted if in one

#list can be also selected specific parts of them
randomNumber = [53, 1, 432, 52, 21, 12, 14.23, 53.23]

#for example max and min
print(max(randomNumber), "bigges number")
print(min(randomNumber), "smallest number")

#same works for string lists

tasks = ["clean", "cook", "eat", "buy", "purchase drink"]

print(max(tasks), "<= alphabetical order biggest")
print(min(tasks), "<= alphabetical order smallest")


