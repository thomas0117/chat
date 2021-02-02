#讀取聊天紀錄並整理
import os 

#讀檔
def read_file(filename):
	lines = []
	with open(filename, 'r',encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
		print('讀檔完畢')
	return lines

#轉換
def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
		elif line == 'Tom':
			person = 'Tom'
		else:
			if person:
				new.append(person + ':' + line)
	return new

#寫檔
def write_file(filename,lines):
	with open(filename,'w',encoding='utf-8-sig') as f: 
		for line in lines:
			f.write(line + '\n')
		print('寫檔完畢') 

def main():
	filename = 'input.txt'
	if os.path.isfile(filename):
		lines = read_file(filename)
		lines = convert(lines)
		# print(lines)
		write_file('output.txt',lines)
	else:
		print('找不到檔案')

main()
	