# Code day 7
# Bitwise

input_code = ["123 -> x",
"456 -> y",
"x AND y -> d",
"x OR y -> e",
"x LSHIFT 2 -> f",
"y RSHIFT 2 -> g",
"NOT x -> h",
"NOT y -> i"]

# and, or, lshift, rightshift, not, assign
# &, |, <<, >>, ~

for i in input_code:
	if i.split()[0].isdigit():
		i.split()[2] = i.split()[0]
		print "assign is: " + str(i.split()[0])

	# elif i.split()[1] == "AND":
	# 	i.split()[4] = i.split()[0] & i.split()[2]
	# 	print "and is: " + str(int(i.split()[0]) & int(i.split()[2]))

	# elif i.split()[0] == "NOT":
	# 	i.split()[3] = ~ i.split()[1]
	# 	print "NOT is: " + str(~i.split()[1])

	# elif i.split()[1] == "OR":
	# 	i.split()[4] = int(i.split()[0]) | int(i.split()[2])
	# 	print "or is: " + str(int(i.split()[0]) | int(i.split()[2]))

	# elif i.split()[1] == "LSHIFT":
	# 	i.split()[4] = int(i.split()[0]) << int(i.split()[2])
	# 	print "lshift is: " + str(int(i.split()[0]) << int(i.split()[2]))

	# elif i.split()[1] == "RSHIFT":
	# 	i.split()[4] = int(i.split()[0]) >> int(i.split()[2])
	# 	print "rshift is: " + str(int(i.split()[0]) >> int(i.split()[2]))



