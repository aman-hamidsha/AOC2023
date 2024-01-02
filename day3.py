file = open('input.txt', 'r')
lines = file.readlines()

#PART 1
newlines = []
for line in lines:
    newlines.append(line.replace('\n','')+'.') # replaces the newlines character with a period to solve edge cases


p1 = 0

for i in range(len(newlines)):
    dig = ""
    invalid = True #at first each line is considered to be be invalid
    
    for j in range(len(newlines[i])): #iterating through each character in a line and checking if it is a digit
        if newlines[i][j].isdigit():
            dig += lines[i][j]
            for m in range(-1,2): 
                for n in range(-1,2): # double for loop to check all surrounding characters, and try-catch to pass errors in edge cases (so that separate code doesnt have be written for i,j = 0,len-1 etc.) 
                    try:
                        if newlines[i+m][j+n] != "." and (not newlines[i+m][j+n].isdigit()): # if it isn't fully surrounded by periods or digits, then it is invalid (it must have contact with a symbol)
                            invalid = False
                            break
                        else:
                            continue
                    except:
                        continue
                        
        else: # if it is not a digit, then if the previous element was a valid digit, then the int of that is added to the final output
            if not invalid:   
                p1+=int(dig) 
            dig = "" #digit is reset to an empty string and flag is set to true (just like in the beginning of the loop)
            invalid = True 
                                          
print(p1)
