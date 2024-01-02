file1 = open('inp.txt', 'r')
lines = file1.readlines()

instruction = ''

coords = []
labels = []
for i in range(len(lines)):
    if i < 2:
        instruction+=lines[i]
    else:
        label, coord = lines[i].split('=')
        labels.append(label)
        coords.append(coord)
instruction = instruction.replace('\n','')

new_labels = []
for label in labels:
    new_labels.append(label.replace(' ',''))

new_coords = []
for coord in coords:
    new_coords.append(coord.replace('\n','').replace('(','').replace(')','').replace(' ',''))


maps = []

for nc in new_coords:
    maps.append(nc.split(','))

dc = {}

for i in range(len(new_labels)):
    dc.update({new_labels[i]:tuple(maps[i])})


count = 0 

checker = 'AAA'

while checker != 'ZZZ':
    for i in range(len(instruction)):
        if instruction[i] == 'R':
            checker = dc.get(checker)[1]
        else:
            checker = dc.get(checker)[0]
        count += 1

print(count)






