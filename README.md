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

        对于字符串，单词和行数的统计，由于前段时间在学习python，所以我第一时间就想到用python写。要实现这些功能，首先就是先找到文件的位置，或者说先打开这个文件，然后遍历这个文件，三个功能对应三个函数，最后调用这三个函数然后输出结果  

### 二、代码说明：  
```python  
#导入argparseku模块，处理命令行参数
import argparse
parser=argparse.ArgumentParser(description='this is wc.exe')
parser.add_argument('-c', dest='char' )
parser.add_argument('-w', dest='word' )
parser.add_argument('-l', dest='line' )
args=parser.parse_args()
```
```python  
def Line_count(args):#统计行数
	lines=0
	with open(args,'r',encoding='utf-8') as f:
		for line in f:
			lines+=1
	return lines
```

```python
def Word_count(args):#统计单词数
	words=0
	with open(args,'r',encoding='utf-8') as f:
		for line in f:
			word=line.split()
			words+=len(word)
	return words
```

```python
def Character_count(args):#统计字符数
	characters=0
	with open(args,'r',encoding='utf-8') as f:
		for line in f:
			characters+=len(line)
	return characters
```

```python
#调用函数并输出结果
if args.line:  #当参数为-l
	line_count=Line_count(args.line)
	print('行数：',line_count)
if args.word:   #当参数为 -w
	word_count=Word_count(args.word)
	print('单词数：',word_count)
if args.char:    ##当参数为 -c
	character_count=Character_count(args.char)
	print('字母数：',character_count)
```

###   

### 三、测试运行  

1. 空文件：

   ![1](https://github.com/dandelionlxj/wc/blob/master/1.png)

2. 只有一个字符的文件：

   ![2](https://github.com/dandelionlxj/wc/blob/master/2.png)

3. 只有一个world单词的文件

   ![3](https://github.com/dandelionlxj/wc/blob/master/3.png)

4. 只有一行 hello world 的文件

   ![4](https://github.com/dandelionlxj/wc/blob/master/4.png)

5. 一个源文件

   ![5](https://github.com/dandelionlxj/wc/blob/master/5.png)

  

### 四、项目小结

   在对于行数、单词和字符的统计的代码写的还算顺利，但是当写到命令行的时候就卡了很久了，花了大量的时间去查了相关的模块，但在命令行参数的使用和理解上还是比较吃力，后来去请教他人才得到解决。通过这次项目让我看到了自身还存在许多不足，知识量还是太少，需要更加刻苦学习来充实自己。