# code_advent_day_10
# elves look, elves say

# import itertools

# input_code = "3113322113";
# iteration_count = 0

# def elf_count(inputs, iteration_count):
# 	print "working"
# 	new_result = ""
# 	if iteration_count < 50:
# 		temp = [''.join(value) for key, value in itertools.groupby(inputs)]
# 		#print temp
# 		for i in temp:
# 			count = len(i)
# 			character = i[0]
# 			new_result = new_result + str(count) + str(character)

# 		#print new_result
# 		elf_count(new_result, iteration_count + 1)

# 	else:
# 		print len(inputs)

# elf_count(input_code, iteration_count)


## ##################################################
# code_advent_day_10
# elves look, elves say

# this method doesn't use recursion. Still really slow :(

import itertools

input_code = "3113322113";
iteration_count = 0

def elf_count(inputs):
	new_result = ""
	temp = [''.join(value) for key, value in itertools.groupby(inputs)]
	for i in temp:
		count = len(i)
		character = i[0]
		new_result = new_result + str(count) + str(character)
	
	return new_result


def iterator(elf_count, n, input):
	for i in range(n):
		print "on step: "+str(i)
		input = elf_count(input)
	return input

print(len(iterator(elf_count,50,input_code)))

