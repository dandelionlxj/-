import argparse
parser=argparse.ArgumentParser(description='this is wc.exe')
parser.add_argument('-c', dest='char' )
parser.add_argument('-w', dest='word' )
parser.add_argument('-l', dest='line' )
args=parser.parse_args()

def Line_count(args):#统计行数
	lines=0
	with open(args,'r',encoding='utf-8') as f:
		for line in f:
			lines+=1
	return lines


def Word_count(args):#统计单词数
	words=0
	with open(args,'r',encoding='utf-8') as f:
		for line in f:
			word=line.split()
			words+=len(word)
	return words


def Character_count(args):#统计字符数
	characters=0
	with open(args,'r',encoding='utf-8') as f:
		for line in f:
			characters+=len(line)
	return characters


if args.line:  #当参数为-l
	line_count=Line_count(args.line)
	print('行数：',line_count)
if args.word:   #当参数为 -w
	word_count=Word_count(args.word)
	print('单词数：',word_count)
if args.char:    ##当参数为 -c
	character_count=Character_count(args.char)
	print('字母数：',character_count)
