# advent day 15
# recipes

import itertools

input_code = ['Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3',
'Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3',
'Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8',
'Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8']

ingredients = {}
max_total_cookie = 1

#permuate through all combos of 4 numbers 0 - 100. Sum must == 100.
mp = []
ap = list(itertools.permutations(range(0,101), len(input_code)))
for i in ap:
	if sum(i) == 100:
		mp.append(i)

for i in input_code:
	ingredient = i.split()[0].replace(':', '')
	capacity = i.split()[2].replace(',', '')
	durability = i.split()[4].replace(',', '')
	flavor = i.split()[6].replace(',', '')
	texture = i.split()[8].replace(',', '')
	calories = i.split()[10]
	ingredients[ingredient] = {"capacity": capacity, "durability": durability, "flavor": flavor, "texture": texture, "calories": calories}

for i in mp:
	first_ing = ingredients[ingredients.keys()[0]]
	second_ing = ingredients[ingredients.keys()[1]]
	third_ing = ingredients[ingredients.keys()[2]]
	fourth_ing = ingredients[ingredients.keys()[3]]
	
	capacity = int(i[0])*int(first_ing["capacity"]) + int(i[1])*int(second_ing["capacity"]) + int(i[2])*int(third_ing["capacity"]) + int(i[3])*int(fourth_ing["capacity"])
	durability = int(i[0])*int(first_ing["durability"]) + int(i[1])*int(second_ing["durability"]) + int(i[2])*int(third_ing["durability"]) + int(i[3])*int(fourth_ing["durability"])
	flavor = int(i[0])*int(first_ing["flavor"]) + int(i[1])*int(second_ing["flavor"]) + int(i[2])*int(third_ing["flavor"]) + int(i[3])*int(fourth_ing["flavor"])
	texture = int(i[0])*int(first_ing["texture"]) + int(i[1])*int(second_ing["texture"]) + int(i[2])*int(third_ing["texture"]) + int(i[3])*int(fourth_ing["texture"])
	calories = int(i[0])*int(first_ing["calories"]) + int(i[1])*int(second_ing["calories"]) + int(i[2])*int(third_ing["calories"]) + int(i[3])*int(fourth_ing["calories"])


	properties = [capacity, durability, flavor, texture]
	for p in range(len(properties)):
		if properties[p] < 0:
			properties[p] = 0

	total_cookie = reduce(lambda x, y: x*y, properties)
	if calories == 500:
		if total_cookie > max_total_cookie:
			max_total_cookie = total_cookie

print max_total_cookie


