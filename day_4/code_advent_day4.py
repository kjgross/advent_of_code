# code_advent_day4

import hashlib

i = 0;
# input_code = "abcdef";
input_code = "ckczppom";
result_found = "FALSE";


while result_found == "FALSE":
	output = hashlib.md5(input_code+str(i)).hexdigest()
	if output[0:6] == "000000":
		result_found = "TRUE"
	else:
		i += 1

print "answer is: " + str(i);