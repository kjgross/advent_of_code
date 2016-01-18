# day 18
# 100 by 100 animated lights

sample_input = open('/Users/kelsey/projects/advent_of_code/day_18/sample_input.txt')
print sample_input
for i in sample_input:
	print i

	print sum(len(line[:]) - (len(unescape(line))) for line in open('/Users/kelsey/projects/advent_of_code/code_advent_day8_input.txt'))