#code_advent_day9
# shortest distance

import itertools;

distances = ['AlphaCentauri to Snowdin = 66',
'AlphaCentauri to Tambi = 28',
'AlphaCentauri to Faerun = 60',
'AlphaCentauri to Norrath = 34',
'AlphaCentauri to Straylight = 34',
'AlphaCentauri to Tristram = 3',
'AlphaCentauri to Arbre = 108',
'Snowdin to Tambi = 22',
'Snowdin to Faerun = 12',
'Snowdin to Norrath = 91',
'Snowdin to Straylight = 121',
'Snowdin to Tristram = 111',
'Snowdin to Arbre = 71',
'Tambi to Faerun = 39',
'Tambi to Norrath = 113',
'Tambi to Straylight = 130',
'Tambi to Tristram = 35',
'Tambi to Arbre = 40',
'Faerun to Norrath = 63',
'Faerun to Straylight = 21',
'Faerun to Tristram = 57',
'Faerun to Arbre = 83',
'Norrath to Straylight = 9',
'Norrath to Tristram = 50',
'Norrath to Arbre = 60',
'Straylight to Tristram = 27',
'Straylight to Arbre = 81',
'Tristram to Arbre = 90']

towns = []
towns_visited = []
lookup_table = {}
longest_distance = 0
# Grab each unique town into an array
for i in distances:
	town1 = i.split()[0]
	town2 = i.split()[2]
	distance = i.split()[4]
	lookup_table[town1+"-"+town2] = distance
	lookup_table[town2+"-"+town1] = distance
	if town1 in towns:
		continue
	else:
		towns.append(town1)
	if town2 in towns:
		continue
	else:
		towns.append(town2)


## Create an array of all possible permutations 
out_list = []
for i in range(1, len(towns)+1):
    out_list.extend(itertools.permutations(towns, len(towns)))


## Iterate through this new list and compare to find shortest distance
for i in out_list:
	if len(i) == len(towns):
		distance = 0
		for j in range(0,len(i)-1):
			distance += int(lookup_table[i[j]+"-"+i[j+1]]);
		if distance > longest_distance:
			longest_distance = distance
print "Longest is: " + str(longest_distance)


