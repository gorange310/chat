
def read_file(input_file):
	lines = []
	with open(input_file, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
		return lines

lines = read_file('input.txt')
print(lines)

