import re
hand = open('regex_sum.txt')
numlist = []

for line in hand:
	line = line.rstrip()
	x = re.findall('[0-9]+', line)
	if len(x) > 0:
		for element in range(len(x)):
			num = float(x[element])
			numlist.append(num)
print(sum(numlist))