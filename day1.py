file = open('input.txt','r')
words = file.readlines()

# PART 1
p1 = 0

for word in words: # iterates through each lines
    num = "" # there will be one output per line
    for char in word: # iterates through each character in the line
        if char.isdigit():  
            num+=char # checks if character is a digit and adds to the string if it is 
    p1+=int(num[0]+num[-1]) #concatenates the first and last character of the string, converts to an integer, and adds to final output

print(p1)

# PART2
p2 = 0
new_words = []

thisdict = { # map to replace text form of the word with digit
  "one": "o1e", # one , eight, etc. are surrounded by extra characters to deal with cases like "oneight"
  "eight": "e8t",
  "zero": "0o",
  "two": "t2o",
  "three": "t3e",
  "five" : "5e",
  "nine" : "9e",
  "four": "4",
  "six": "6",
  "seven": "7",
}

# loop iterating through each character in each line and swapping 
# the keys with their coresponding values (swapping texts with digits)
# and appending each output to a new list
for word in words:
    new_word = ""
    for key in thisdict.keys():
        new_word = word.replace(key,thisdict.get(key))
        word = new_word
    new_words.append(new_word)

# same logic as part 1
for new_word in new_words:
    num = ""
    for char in new_word:
        if char.isdigit():
            num+=char
    p2+=int(num[0]+num[-1])


print(p2)

