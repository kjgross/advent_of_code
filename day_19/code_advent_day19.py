# code_advent_day19
# replace one step

# 193

input_rules = ['Al => ThF',
'Al => ThRnFAr',
'B => BCa',
'B => TiB',
'B => TiRnFAr',
'Ca => CaCa',
'Ca => PB',
'Ca => PRnFAr',
'Ca => SiRnFYFAr',
'Ca => SiRnMgAr',
'Ca => SiTh',
'F => CaF',
'F => PMg',
'F => SiAl',
'H => CRnAlAr',
'H => CRnFYFYFAr',
'H => CRnFYMgAr',
'H => CRnMgYFAr',
'H => HCa',
'H => NRnFYFAr',
'H => NRnMgAr',
'H => NTh',
'H => OB',
'H => ORnFAr',
'Mg => BF',
'Mg => TiMg',
'N => CRnFAr',
'N => HSi',
'O => CRnFYFAr',
'O => CRnMgAr',
'O => HP',
'O => NRnFAr',
'O => OTi',
'P => CaP',
'P => PTi',
'P => SiRnFAr',
'Si => CaSi',
'Th => ThCa',
'Ti => BP',
'Ti => TiTi',
'e => HF',
'e => NAl',
'e => OMg']

input_word = "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"



def rule_by_letter(input_rules):
	rule_dict = {}
	for i in input_rules:
		if i.split()[0] in rule_dict.keys():
			rule_dict[i.split()[0]].append(i.split()[2])
		else:
			rule_dict[i.split()[0]] = [i.split()[2]]
	return rule_dict

# def word_letter_count(input_word):
# 	letter_count = {}
# 	for i in input_word:
# 		if i in letter_count.keys():
# 			letter_count[i] += 1
# 		else:
# 			letter_count[i] = 1
# 	print letter_count
# 	return letter_count

def main(input_rules, input_word):
	count = 0
	new_words = []
	rule_dict = rule_by_letter(input_rules)
	#letter_count = word_letter_count(input_word)
	for i in range(0,len(input_word)):
		if input_word[i] in rule_dict.keys():
			for j in rule_dict[input_word[i]]:
				if i > 0:
					temp = str(input_word[:i]) + j + str(input_word[i+1:])
					if temp not in new_words:
						new_words.append(temp)
				else:
					temp = j + str(input_word[i+1:])
					if temp not in new_words:
						new_words.append(temp)
	print len(new_words)
				
main(input_rules, input_word)






