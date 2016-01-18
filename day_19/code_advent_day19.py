# code_advent_day19
# replace one step


# input_rules = ['H => HO',
# 'H => OH',
# 'O => HH']

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

magic_medicine = "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"

input_word = "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"
#input_word = "HOHOHO"

def rule_by_letter(input_rules):
	rule_dict = {}
	for i in input_rules:
		if i.split()[0] in rule_dict.keys():
			rule_dict[i.split()[0]].append(i.split()[2])
		else:
			rule_dict[i.split()[0]] = [i.split()[2]]
	return rule_dict



def main(input_rules, input_word):
	count = 0
	new_words = []
	rule_dict = rule_by_letter(input_rules)
	for i in rule_dict.keys():
		for j in range(0, len(input_word)):
			if len(rule_dict[i])>1:
				for k in rule_dict[i]:
					if input_word[j:j+len(i)] == i:
						temp = str(input_word[:j]) + k + str(input_word[j+len(i):])
						if temp not in new_words:
							new_words.append(temp)

			else:
				if input_word[j:j+len(i)] == i:
					temp = str(input_word[:j]) + str(rule_dict[i][0]) + str(input_word[j+len(i):])
					if temp not in new_words:
						new_words.append(temp)
	print len(new_words)



			
main(input_rules, input_word)






