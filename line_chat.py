# line chat convert
def read_file(input_file):
	lines = []
	with open(input_file, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
		return lines

def convert(lines, person_a, person_b):
	person = None
	person_a_word_count = 0
	person_b_word_count = 0
	person_a_sticker_count = 0
	person_b_sticker_count = 0
	person_a_picture_count = 0
	person_b_picture_count = 0
	person_a_file_count = 0
	person_b_file_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == person_a:
			if s[2] == '貼圖':
				person_a_sticker_count += 1
			elif s[2] == '圖片':
				person_a_picture_count += 1
			elif s[2] == '檔案':
				person_a_file_count += 1
			else:
				for msg in s[2:]:
					person_a_word_count += len(msg)
		elif name == person_b:
			if s[2] == '貼圖':
				person_b_sticker_count += 1
			elif s[2] == '圖片':
				person_b_picture_count += 1
			elif s[2] == '檔案':
				person_b_file_count += 1
			else:
				for msg in s[2:]:
					person_b_word_count += len(msg) 
	print(person_a, 'sent ', person_a_sticker_count, ' stickers.')
	print(person_a, 'sent ', person_a_picture_count, ' pitures.')
	print(person_a, 'sent ', person_a_file_count, ' files.')
	print(person_a, 'sent ', person_a_word_count, ' letters.')

	print(person_b, 'sent ', person_b_sticker_count, ' stickers.')
	print(person_b, 'sent ', person_b_picture_count, ' pitures.')
	print(person_b, 'sent ', person_b_file_count, ' files.')
	print(person_b, 'sent ', person_b_word_count, ' letters.')
	return lines


def write_file(output_file, lines):
	with open(output_file, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	input_file = input('Please key in the file name: ')
	person_a = input('Person_a in the chat: ')
	person_b = input('Please_b in the chat: ')
	lines = read_file(input_file)
	lines = convert(lines, person_a, person_b)
	#write_file('ouput.txt', lines)

main()