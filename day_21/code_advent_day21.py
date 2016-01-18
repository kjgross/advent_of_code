# day 21
# battle game

#you have 8 hit points, 5 damage, and 5 armor, 
# and that the boss has 12 hit points, 7 damage, and 2 armor:

# boss = {"Hit_Points": 12,
# "Damage": 7,
# "Armor": 2}

# player = {"Hit_Points": 8,
# "Damage": 4,
# "Armor": 5}

boss = {"Hit_Points": 109,
"Damage": 8,
"Armor": 2}

player = {"Hit_Points": 100,
"Damage": 0,
"Armor": 0}

# so long as I pick d & a such that (d-2)*100 >= (8-a)*109
#       100d - 200 >= 872 - 109a
# i.e.  100d + 109a >= 1072

# so min(cost) of (1)W + (0-1)M + (0-2)R such that 100d + 109a >= 1072

#[cost, d, a]
Weapons = [[8,4,0],[10,5,0],[25,6,0],[40,7,0],[74,8,0]]
Armor = [[13,0,1],[31,0,2],[53,0,3],[75,0,4],[102,0,5]]
Rings = [[25,1,0],[50,2,0],[100,3,0],[20,0,1],[40,0,2],[80,0,3]]

def combos(listA, listB, starter):
	combo= starter
	for i in listA:
		combo.append(i)
	if listA == listB:
		for i in range(0,len(listA)):
			for j in range(0,len(listB)):
				if listA[i] != listB[j]:
					d = listA[i][1] + listB[j][1]
					a = listA[i][2] + listB[j][2]
					cost = listA[i][0] + listB[j][0] 
					combo.append([cost,d,a])
	else:
		for i in range(0,len(listA)):
			for j in range(0,len(listB)):
				d = listA[i][1] + listB[j][1]
				a = listA[i][2] + listB[j][2]
				cost = listA[i][0] + listB[j][0] 
				combo.append([cost,d,a])
	return combo

def main_win():
	options = []
	min_cost = 10000
	max_cost = 0
	all_rings = combos(Rings,Rings,[[0,0,0]])
	wps_amr = combos(Weapons,Armor,[])
	for i in wps_amr:
		for j in all_rings:
			d = i[1]+j[1]
			a = i[2]+j[2]
			cost = i[0]+j[0]
			options.append([cost,d,a])
			if d*100 + a*109 >= 1072:
				if cost < min_cost:
					min_cost = cost
			if d*100 + a*109 < 1072:
				if cost > max_cost:
					max_cost = cost
	print "Min cost is: " + str(min_cost)
	print "Max cost is: " + str(max_cost)
	return options

main_win()

## #####################################################
## This part plays the game, but isn't needed.

# def hit_calc(a, b):
# 	if int(a["Damage"]) - int(b["Armor"]) > 1:
# 		hit = int(a["Damage"]) - int(b["Armor"])
# 	else:
# 		hit = 1
# 	return hit


# def game(boss, player):
# 	winner = ""
# 	boss_hit = hit_calc(boss, player)
# 	player_hit = hit_calc(player, boss)
# 	if int(boss["Hit_Points"])/player_hit <= int(player["Hit_Points"])/boss_hit:
# 		winner = "player"
# 	else:
# 		winner = "boss"
# 	return winner


## ###################################################

