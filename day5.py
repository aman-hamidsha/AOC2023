file = open('input.txt','r')
lines = file.readlines()

#PART 1

seeds_list = []
datas = []

for line in lines:
    if ":" in line: #signifies the beginning of each map
        y = [] 
        datas.append(y)
        label , data = line.split(":")
        
        if (len(seeds_list) == 0): #first line is the list of seeeds
            seeds_list.append(data)
    else: 
        y.append(line) #all other numbers are grouped into sublists and appended to a large list for all the data

seeds = seeds_list[0].split()
seeds = [int(x) for x in seeds] # list of seeds

datas = [x for x in datas if x != ""]

new = []
for i in datas:
    i = [x for x in i if x != '']
    new.append(i)

new.remove(new[0])

final = [] # final flattened list, cleaned up only numbers present
for thing in new:
    new_thing = []
    for item in thing:
        x = item.split()
        for split in x:
            new_thing.append(int(split))

    final.append(new_thing)
        


d = [] #destination ranges
s = [] #source ranges
l = [] # range lengths

for i in final:
    # source, destination , and length for each line
    dr = [] 
    sr = []
    lr = []
    for j in range(0,len(i),3): # n,n+3,n+6 etc. is all destination 
        dr.append(i[j])
    for j in range(1,len(i),3): # n+1, n+4. n+7 etc. source 
        sr.append(i[j])
    for j in range(2,len(i),3): # n+2, n+5, n+8, etc lengths
        lr.append(i[j])

    d.append(dr)
    s.append(sr)
    l.append(lr)

minimum = float('inf') #python infinity, cool right?

for seed in seeds: #finding the minimum of the seeds
    for m in range(len(d)):
        for ele in s[m]:
            x = s[m].index(ele)
            if seed >= ele  and seed < ele + l[m][x]: # if seed is within the range, it is set equal to the destination + the difference
                diff = seed - ele
                seed = d[m][x] + diff 
                break
    if seed < minimum:
        minimum = seed
        
p1 = minimum
print(p1)
