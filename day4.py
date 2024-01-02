file = open('input.txt','r')
lines = file.readlines()

#PART 1 AND 2
p1 = 0
p2 = 0
ids = [] #id numbers list
cards_info = {} # dictionary with id number as key and number of winning cards as value
copies = [] #list to store winning copies

for line in lines:
    score = 0
    cardno, info = line.split(":") # "info" is everything that comes after the colon 
    
    card, id1 = cardno.split()
    ids.append(id1)

    

    winning, trial = info.split("|") # "winning" is before the "|" and "trial" is after "|"
    
    # extracting each of the scores
    winning_nos = winning.split() 
    trial_nos = trial.split()

    x = int(id1) 
    count = 0

    for trial_no in trial_nos:
        if trial_no in winning_nos: # case for winning number present in the trial
            if score == 0:
                score += 1
            else:
                score *=2 # each match after the first doubles the point value
            
            x += 1 
            count +=1
            copies.append(x) # appending a copy of next number to the winning copies

    p1 += score
    cards_info.update({int(id1):count})




for item in copies: # formula that appends "number of winning cards" copies of card number n+1 to list given a card number n
    x = cards_info.get(item)
    v = item + 1
    for i in range(x):
        copies.append(v)
        v += 1


print(p1)

p2 = len(copies)+len(ids) #copies + originals is the total

print(p2)




