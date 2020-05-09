def read_file(input_file):
	lines = []
	with open(input_file, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
		return lines

def convert(lines, person_a, person_b):
	new = []
	person = None
	for line in lines:
		if line == person_a:
			person = person_a
			continue
		elif line == person_b:
			person = person_b
			continue
		if person:
			new.append(person + ': ' + line)
	return new

def write_file(output_file, lines):
	with open(output_file, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines, 'Allen', 'Tom')
	write_file('ouput.txt', lines)

main()