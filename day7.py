file1 = open('inp.txt', 'r')
lines = file1.readlines()

# PART 1


hands = []
bids = []
for line in lines:
    hand, bid = line.split()
    hands.append(hand)
    bids.append(int(bid))


bidder = dict(zip(hands,bids)) 
types = [] 

for c in hands: # based on the number of different strengths of cards, a dictionary is made, and the dictionary is used to determine the type of the card
    type = 0
    w2s = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    w2_counts = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    zz = dict(zip(w2s,w2_counts))
    for char in c:
        for w2 in w2s:
            if char == w2:
                zz[w2] += 1
    fives = len([x for x in zz.values() if x == 5])
    fours = len([x for x in zz.values() if x == 4])
    threes = len([x for x in zz.values() if x == 3])
    twos = len([x for x in zz.values() if x == 2])

    if fives > 0:
        type += 6
    elif fours > 0:
        type += 5
    elif threes > 0 and twos > 0:
        type += 4
    elif threes > 0: 
        type += 3
    elif twos > 1:
        type += 2
    elif twos == 1:
        type += 1
    else:
        type += 0
    types.append(type)

# separate lists of cards of each type
sixs = []
fivs = []
frs = []
thrs = []
tws = []
ons = []
zrs = []

tys = dict(zip(hands, types)) # mapping each card to its type 

# appending card based on its type to the appropriate list
for key in tys.keys():
    if tys.get(key) == 6:
        sixs.append(key)
    elif tys.get(key) == 5:
        fivs.append(key)
    elif tys.get(key) == 4:
        frs.append(key)
    elif tys.get(key) == 3:
        thrs.append(key)
    elif tys.get(key) == 2:
        tws.append(key)
    elif tys.get(key) == 1:
        ons.append(key)
    else:
        zrs.append(key)



strengths = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


#bubble sort based on strength value and if strengths are equal next character is compared
def bubbleSort(ls):
    n = len(ls)
    for i in range(n):
        sweep(ls)
    return ls

def sweep(ls):
    n = len(ls)
    first_index = 0
    second_index = 1

    while second_index < n:
        firstVal = ls[first_index]
        secondVal = ls[second_index]

        for j in range(len(firstVal)):
            if strengths.index(firstVal[j]) > strengths.index(secondVal[j]):
                ls[first_index], ls[second_index] = secondVal, firstVal
                break
            elif strengths.index(firstVal[j]) == strengths.index(secondVal[j]):
                continue
            else:
                break
    

        first_index += 1
        second_index += 1


#adding in order from high cards to five of a kinds
        
almost = bubbleSort(zrs)+bubbleSort(ons)+bubbleSort(tws)+bubbleSort(thrs)+bubbleSort(frs)+bubbleSort(fivs)+bubbleSort(sixs)


# calculates total scores by ranking cards and then multiplying rank with bid using a map
ranks = []

for f in almost:
    ranks.append(almost.index(f)+1)

card_rank = dict(zip(almost,ranks))



tots = {}


for key1 in card_rank.keys():
    for key2 in bidder.keys():
        if key1 == key2:
            tots.update({card_rank.get(key1):bidder.get(key2)})

p1 = 0

for k in tots.keys():
    p1 += k * tots.get(k)



print(p1) 
