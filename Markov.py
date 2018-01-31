# -*- coding: utf-8 -*-

import re
import random
import jieba

def split_string(_in):
	return re.findall(r"[\w']+|[.,!?;]", _in)

markov_dict = {"_START": []}

def update_an_entry(markov_dict, first_word, next_word):
	if first_word not in markov_dict:
		markov_dict[first_word] = [next_word]
	else:
		markov_dict[first_word].append(next_word)


def train(file):
	if is_Chinese == True:
		start = []
		length = len(file)
		for index, word in enumerate(file):
			if index == length:
				#print "done"
				break
			if index == 0:
				update_an_entry(markov_dict, "_START", word)
			elif file[index - 1].encode("utf-8") in ["。", "！", "？"]:
				update_an_entry(markov_dict, "_START", word)
				update_an_entry(markov_dict, file[index - 1], word)
			else:
				#print file[index - 1], word
				update_an_entry(markov_dict, file[index - 1], word)
	else:
		start = []
		length = len(file)
		for index, word in enumerate(file):
			if index == length:
				#print "done"
				break
			if index == 0:
				update_an_entry(markov_dict, "_START", word)
			elif file[index - 1]in [".", "!", "?"]:
				update_an_entry(markov_dict, "_START", word)
				update_an_entry(markov_dict, file[index - 1], word)
			else:
				#print file[index - 1], word
				update_an_entry(markov_dict, file[index - 1], word)

file = open('test_file.txt', 'r')
file_in_string = ""

for line in file:
	file_in_string += line

is_Chinese = False

if is_Chinese:
	cut = jieba.cut(file_in_string)
	file = [i for i in cut if i.encode("utf-8") not in["\n", "(", ")", "-", " "]]
else:
	file = split_string(file_in_string)

#print file


train(file)


'''
def find_the_largest_word(_in):
	current_frequency = 0
	current_word = None
	for i in _in:
		if i[1] > current_frequency:
			current_word = i[0]
	return current_word
'''

def generate_one_sentence(markov_dict):
	if is_Chinese:
		result = []
		first_word = random.choice(markov_dict["_START"])
		result.append(first_word)
		next_word = random.choice(markov_dict[first_word])
		result.append(next_word)
		while next_word.encode("utf-8") not in ["。", "！", "？"]:
			next_word = random.choice(markov_dict[next_word])
			result.append(next_word)
			#print result
		return result
	else:
		result = []
		first_word = random.choice(markov_dict["_START"])
		result.append(first_word)
		next_word = random.choice(markov_dict[first_word])
		result.append(next_word)
		while next_word not in [".", "!", "?"]:
			next_word = random.choice(markov_dict[next_word])
			result.append(next_word)
			#print result
		return result

final = ""

for i in range(10):
	if is_Chinese:
		result = [i.encode("utf-8") for i in generate_one_sentence(markov_dict)]
		print "".join(result)
	else:
		result = [i for i in generate_one_sentence(markov_dict)]
		for index, i in enumerate(result):
			if index < len(result) and result[index + 1] in [".", ",", "!", "?", ";", "-"]:
				result[index] = result[index] + result[index + 1] + "\n"
				result.remove(result[index + 1])
		print " ".join(result)
	

print final
