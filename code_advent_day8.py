## Day 8: Matchsticks

## Ben suggests learn regex expression for finding the whatever \x__. 
# Perhaps a higher level fxn?
import re

literal = 0
in_memory = 0
#input_code = ""
#input_code = ["abc"]
#input_code= "aaa\"aaa\n"
#input_code = ["aaa\"aaa","abc"] #3+2=5
#input_code = "\x27"
#input_code = ["\x27","abc"]  #(6-1)+(5-3) = 7

def unescape(line):
    #line = re.sub('\A"(.*)"\Z', 'Z', line) # remove quotes
    line = re.sub(r'\A"', 'A', line) # remove quotes
    line = re.sub(r'\\"', 'N', line) # remove quote
    line = re.sub(r'\\\\', 'S', line) # remove slash
    line = re.sub(r'\\x[0-9a-fA-F]{2}', 'H', line) # remove hex
    return line

print sum(len(line[:]) - (len(unescape(line))) for line in open('/Users/kelsey/projects/advent_of_code/code_advent_day8_input.txt'))

#print sum(len(input_code[:-1]) - len(eval(input_code)) for input_code in open('/Users/kelsey/projects/advent_of_code/code_advent_day8_input.txt'))
