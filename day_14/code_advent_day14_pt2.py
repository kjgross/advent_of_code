# code adavent day 14
# reindeer races


input_code = ['Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.',
'Cupid can fly 22 km/s for 2 seconds, but then must rest for 41 seconds.',
'Rudolph can fly 11 km/s for 5 seconds, but then must rest for 48 seconds.',
'Donner can fly 28 km/s for 5 seconds, but then must rest for 134 seconds.',
'Dasher can fly 4 km/s for 16 seconds, but then must rest for 55 seconds.',
'Blitzen can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.',
'Prancer can fly 3 km/s for 21 seconds, but then must rest for 40 seconds.',
'Comet can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.',
'Vixen can fly 18 km/s for 5 seconds, but then must rest for 84 seconds.']

reindeer_trackers = {}
reindeer_score = {}
reindeer_data = []
total_time = 2503
current_time = 1


for i in input_code:
	deer = {}
	name = i.split()[0]
	deer["name"] = name
	deer["fly_distance"] = int(i.split()[3])
	deer["fly_time"] = int(i.split()[6])
	deer["rest_time"] = int(i.split()[13])
	deer["cycle_time"] = deer["fly_time"] + deer["rest_time"]
	reindeer_trackers[name] = 0
	reindeer_score[name] = 0
	reindeer_data.append(deer)


while current_time <= total_time:
	for r in reindeer_data:
	#check if resting or flying 
		if current_time % r["cycle_time"] <= r["fly_time"]:
			# update reindeer array with new distances
			reindeer_trackers[r["name"]] += r["fly_distance"]
	# update score with current leaders
	for i in reindeer_trackers:
		if reindeer_trackers[i] == max(reindeer_trackers.values()):
			reindeer_score[str(i)] += 1
	current_time += 1



print "distances are: " + str(reindeer_trackers)
print "scores are: " + str(reindeer_score)
print "max score is: " + str(max(reindeer_score.values()))

# Answers are:

#distances are: {'Vixen': 3114, 'Donner': 3052, 'Rudolph': 3157, 'Prancer': 2712, 'Cupid': 3872, 'Dancer': 3051, 'Blitzen': 3444, 'Comet': 2880, 'Dasher': 2444}
#scores are: {'Vixen': 21, 'Donner': 175, 'Rudolph': 0, 'Prancer': 0, 'Cupid': 2298, 'Dancer': 8, 'Blitzen': 21, 'Comet': 18, 'Dasher': 0}
#max score is: 2298
	
