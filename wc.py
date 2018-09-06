file_name='D:/python/alien/button.py'
def Line_count(file_name):#统计行数
	lines=0
	with open(file_name,'r',encoding='utf-8') as f:
		for line in f:
			lines+=1
	return lines


def Word_count(file_name):#统计单词数
	words=0
	with open(file_name,'r',encoding='utf-8') as f:
		for line in f:
			word=line.split()
			words+=len(word)
	return words


def Character_count(file_name):
	characters=0
	with open(file_name,'r',encoding='utf-8') as f:
		for line in f:
			characters+=len(line)
	return characters

line_count=Line_count(file_name)
word_count=Word_count(file_name)
character_count=Character_count(file_name)




print('行数：',line_count)
print('单词数：',word_count)
print('字母数：',character_count)
