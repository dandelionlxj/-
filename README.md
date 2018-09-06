GitHub地址：[link] https://github.com/dandelionlxj/wc  


| PSP2.1                                | Personal Software Process Stages      | 预估耗时（分钟） | 实际耗时（分钟） |
| ------------------------------------- | ------------------------------------- | ---------------- | ---------------- |
| Planning                              | 计划                                  |  20                |                  |
| Estimate                              | 估计这个任务需要多少时间              |      10            |     10             |
| Development                           | 开发                                  |  1440                |                  |
| Analysis                              | 需求分析 (包括学习新技术)             |  60               |                  |
| Design Spec                           | 生成设计文档                          |  60                |                  |
| Design Review                         | 设计复审 (和同事审核设计文档)         |     60             |                  |
| Coding Standard                       | 代码规范 (为目前的开发制定合适的规范) |      60            |                  |
| Design                                | 具体设计                              |     60             |                  |
| Coding                                | 具体编码                              |      60            |                  |
| Code Review                           | 代码复审                              |   30               |                  |
| · Test                                | 测试（自我测试，修改代码，提交修改）  |     30             |                  |
| Reporting                             | 报告                                  |  60                |                  |
| Test Report                           | 测试报告                              |    60              |                  |
| Size Measurement                      | 计算工作量                            |      10            |                  |
| Postmortem & Process Improvement Plan | 事后总结, 并提出过程改进计划          |         30         |                  |
|                                       | 合计                                  |     2030             |                  |

### 一、解题思路：  

​        对于字符串，单词和行数的统计，由于前段时间在学习python，所以我第一时间就想到用python写。要实现这些功能，首先就是先找到文件的位置，或者说先打开这个文件，然后遍历这个文件，三个功能对应三个函数，最后调用这三个函数然后输出结果  

### 二、代码说明：  
```python  
def Line_count(file_name):#统计行数
	lines=0
	with open(file_name,'r',encoding='utf-8') as f:   #打开文件
		for line in f:    #遍历文件
			lines+=1
	return lines
```

```python
def Word_count(file_name):#统计单词数
	words=0
	with open(file_name,'r',encoding='utf-8') as f:
		for line in f:
			word=line.split()
			words+=len(word)
	return words
```

```python
def Character_count(file_name): #统计字符串
	characters=0
	with open(file_name,'r',encoding='utf-8') as f:
		for line in f:
			characters+=len(line)
	return characters
```

```python
#调用函数并输出结果
line_count=Line_count(file_name)
word_count=Word_count(file_name)
character_count=Character_count(file_name)

print('行数：',line_count)
print('单词数：',word_count)
print('字母数：',character_count)
```

