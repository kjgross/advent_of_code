# day 20
# sequential infinite lists - elves giving gifts

# what's the first number where the sum of it's factors
# is >= magic_number

import math
magic_number = 36000000

def factors(x):
	# find factors less than sqrt(x). 
	# Then use their inverse to quickly fill in the rest.
	small_factors, big_factors = [], []
	for i in range(1,int(math.sqrt(x)) + 1):
		if x % i == 0:
			small_factors.append(i)
	for j in small_factors:
		if x / j != j:
			big_factors.append(x/j)		
	return small_factors + big_factors 

def main(mn):
	factor_array = []
	i = 0
	part_1, part_2 = None, None
	# Solve parts one and two simultaneously to save time
	while not part_1 or not part_2:
		i+=1
		factor_array = factors(i)
		if not part_1:
			if sum(factor_array) * 10 >= int(mn):
				part_1 = i
		if not part_2:
			if sum(w for w in factor_array if i/w <=50)*11 >= int(mn):
				part_2 = i
	print "answer is: " + str(part_1) + " & " + str(part_2)


main(magic_number)
