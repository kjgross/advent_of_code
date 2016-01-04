
import itertools
magic_sum = 25
#magic_sum = 150

input_code = [20, 15, 10, 5, 5]
input_code_r = input_code[:]
#input_code = [43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38]
input_code.sort()
input_code_r.sort(reverse=True)

def set_bound(input_code):
	current_count = 0
	for i in range(0, len(input_code)-1):
		if current_count + input_code[i] <= magic_sum:
			current_count += input_code[i]
		else:
			max_array_len = i + 1
			return max_array_len


def main(input_code, min_len, max_len):
	count = 0
	for j in range(min_len, max_len):
		print "on permutations of length: " + str(j)
		for i in list(itertools.permutations(input_code, j)):
			if sum(list(i)) == magic_sum:
				count += 1

	for i in input_code:
		if i == magic_sum:
			count += 1

	print count

max_len = set_bound(input_code)
min_len = set_bound(input_code_r)

main(input_code, min_len, 5)
