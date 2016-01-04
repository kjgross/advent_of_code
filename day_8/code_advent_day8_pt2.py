## Day 8: Matchsticks pt2

## Ben suggests learn regex expression for finding the whatever \x__. 
# Perhaps a higher level fxn?
import re


print sum(len(re.escape(input_code)) - len(input_code[:-1]) for input_code in open('/Users/kelsey/projects/advent_of_code/code_advent_day8_input.txt'))
