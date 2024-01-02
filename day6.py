file1 = open('inp.txt', 'r')
lines = file1.readlines()


#PART 1
ds = []

#pairing up the times and distances to form the dictionary q
for line in lines:
    idd, x = line.split(':')
    y = x.split()
    y = [int(a) for a in y]
    ds.append(y)

q = dict(zip(ds[0],ds[1]))


p1 = 1
for key in q.keys():
    p2 = 0
    for i in range(key+1): # for each time in the possible times, the distancce is calculated and if the distance beats winning distance then counter is incremented
        s = i 
        t = key - i
        d = s * t 
        if d > q.get(key):
            p2 += 1
    p1 *= p2 # all counts are multiplied together to make the final result

print(p1)

#PART 2

#brute-force approach, same logic as part 1 but all the strings are concatenated and the number for the one race is calculated
ds1 = []

for line in lines:
    idd, x = line.split(':')
    y = x.split()
    t = ""
    for y1 in y:
        t+=y1
    ds1.append(int(t)) # the number is calculated by concatenation of the sstring

p2 = 0
for i in range(ds1[0]+1):
    s = i
    t = ds1[0] - i
    d = s * t 
    if d > ds1[1]:
        p2 += 1 # same logic as part 1
print(p2)
