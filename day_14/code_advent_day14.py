# code adavent day 14
# reindeer races

# Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
# Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.

# 1000s comet = 1120   and dancer = 1056


input_code = ['Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.',
'Cupid can fly 22 km/s for 2 seconds, but then must rest for 41 seconds.',
'Rudolph can fly 11 km/s for 5 seconds, but then must rest for 48 seconds.',
'Donner can fly 28 km/s for 5 seconds, but then must rest for 134 seconds.',
'Dasher can fly 4 km/s for 16 seconds, but then must rest for 55 seconds.',
'Blitzen can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.',
'Prancer can fly 3 km/s for 21 seconds, but then must rest for 40 seconds.',
'Comet can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.',
'Vixen can fly 18 km/s for 5 seconds, but then must rest for 84 seconds.']



reindeer_trackers = []
total_time = 2503

for i in input_code:
	name = i.split()[0]
	fly_distance = int(i.split()[3])
	fly_time = int(i.split()[6])
	rest_time = int(i.split()[13])
	cycle_time = fly_time + rest_time
	reindeer_remainder = total_time % cycle_time
	ftd = fly_distance * fly_time

	# check if flying or resting
	if reindeer_remainder > fly_time: #reindeer resting
		reindeer_distance = total_time/cycle_time*ftd + ftd
	else:
		reindeer_distance = total_time/cycle_time*ftd + ftd/reindeer_remainder #reindeer flying
	reindeer_trackers.append(reindeer_distance)


print max(reindeer_trackers)
	
