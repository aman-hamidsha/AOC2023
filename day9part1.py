file1 = open('inp.txt', 'r')
lines = file1.readlines()

newlines = []
for line in lines:
	newlines.append(line.replace('\n',''))

sequences = []

for nl in newlines:
	sequences.append([int(x) for x in nl.split()])



def differ(ls):
	output = []
	for i in range(len(ls)-1):
		output.append(ls[i+1]-ls[i])
	return output

final_sum = 0
for sequence in sequences:
	s = 0
	a = []
	a.append(sequence)
	while not all(ele == 0 for ele in sequence):
		sequence = differ(sequence)
		a.append(sequence)
	for item in a:
		s+= item[-1]
	final_sum+=s

print(final_sum)
