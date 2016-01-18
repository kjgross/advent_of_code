# day 21
# battle game

#you have 8 hit points, 5 damage, and 5 armor, 
# and that the boss has 12 hit points, 7 damage, and 2 armor:

## MIN COST IS 91

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
"Damage": 1,
"Armor": 1}

# so long as I pick d & a such that d-2 >= 8-a  i.e. d+a >= 10
# so min(cost) of (1)W + (0-1)M + (0-2)R such that d+d+d+a+a+a >=10

#[cost, d+a]
Weapons = [[8,4],[10,5],[25,6],[40,7],[74,8]]
Armor = [[13,1],[31,2],[53,3],[75,4],[102,5]]
Rings = [[25,1],[50,2],[100,3],[20,1],[40,2],[80,3]]

def combos(listA, listB, starter):
	combo= starter
	for i in listA:
		combo.append(i)
	if listA == listB:
		for i in range(0,len(listA)-1):
			for j in range(i+1,len(listB)):
				ad = listA[i][1] + listB[j][1]
				cost = listA[i][0] + listB[j][0] 
				combo.append([cost,ad])
		print combo
	else:
		for i in range(0,len(listA)):
			for j in range(0,len(listB)):
				ad = listA[i][1] + listB[j][1]
				cost = listA[i][0] + listB[j][0] 
				combo.append([cost,ad])
	return combo

min_cost = 10000
all_rings = combos(Rings,Rings,[[0,0]])
wps_amr = combos(Weapons,Armor,[])
for i in wps_amr:
	for j in all_rings:
		ad = i[1]+j[1]
		cost = i[0]+j[0]
		if ad >= 10:
			if cost < min_cost:
				min_cost = cost
print min_cost


## #####################################################
## This part plays the game, but isn't strictly necessary.

# def hit_calc(a, b):
# 	if int(a["Damage"]) - int(b["Armor"]) > 1:
# 		hit = int(a["Damage"]) - int(b["Armor"])
# 	else:
# 		hit = 1
# 	return hit



# def game(boss, player):
# 	boss_hit = hit_calc(boss, player)
# 	player_hit = hit_calc(player, boss)
# 	if int(boss["Hit_Points"])/player_hit <= int(player["Hit_Points"])/boss_hit:
# 		print "player_wins"
# 	else:
# 		print "boss_wins"

# game(boss,player)