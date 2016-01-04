#code advent day 11
# santas password

import itertools

def sequence(password):
	for i in range(0,len(password)-2):
		if ord(password[i])+2 == ord(password[i+1])+1 == ord(password[i+2]):
			return "true"
	return "false"

def non_confusing(password):
	for i in range(0, len(password)):
		if password[i] in ("i","o", "l"):
			return "false"
	return "true"

def two_doubles(password):
	count = 0
	temp = [''.join(value) for key, value in itertools.groupby(password)]
	for j in temp:
		if len(j) > 1:
			count += 1
	if count > 1:
		return "true"
	else:
		return "false"

## attempted to do via recursion but it maxed out
# def increment2(password, i):
# 	if password[i] == 'z':
# 		if i==7:
# 			temp = password[:i] + 'a' 
# 			print "part a is "+temp
# 			increment(temp, i-1)
# 		else:
# 			temp = password[:i] + 'a' + password[i+1:]
# 			print "part a is "+temp
# 			increment(temp, i-1)
# 	else: #ord(password[i]) < 122:
# 		newpass = password[:i] + chr(ord(password[i])+1) + password[i+1:]
# 		print "part b newpass is: "+newpass
# 		return newpass

def increment(password):
	a = list(map(ord,password))
	index = -1

	while True:
		a[index] += 1
		if a[index] <= ord('z'):
			break
		else:
			a[index] = ord('a')
			index -= 1

	return ''.join(map(chr,a))

		
def check_3_rules(new_password):
	verdict = "false"
	if sequence(new_password) == "true":
		if non_confusing(new_password) == "true":
			if two_doubles(new_password) == "true":
				verdict = "true"
	return verdict


def main(password):
	while True:
		password = increment(password)
		if check_3_rules(password) == "true":
			return password


#password = 'hxbxwxba'
password = 'hxbxxyzz'
print main(password)
