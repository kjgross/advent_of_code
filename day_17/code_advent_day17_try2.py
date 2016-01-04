# advent of code day 17
# eggnog tubberware

#magic_sum = 25
magic_sum = 150

#input_code = [20, 15, 10, 5, 5]
input_code = [43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38]

# cause generators are awesome!

# 1. split list into two
# 2. run permutation (or power set) on each of the two new lists
# 3. sum every permutation in the two new lists individually.
# 4. compare each sum of the first list to every sum in the second list looking for an exact match



def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item



part_a = powerset(input_code[:len(input_code)/2])
part_b = powerset(input_code[len(input_code)/2:])
print part_b
print part_a
part_asum = []
part_bsum = []
count = 0

for i in part_a:
	part_asum.append(int(sum(i)))

for i in part_b:
	part_bsum.append(int(sum(i)))

for i in part_asum:
	for j in part_bsum:
		if i+j==magic_sum:
			count+=1


print count

