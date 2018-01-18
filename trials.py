import numpy

wins = 0
for i in range(10000):
	doors = [1, 2, 3]
	# Randomly pick a door for the car to be behind
	car = numpy.random.randint(1, 4)

	# Randomly select a door and remove it
	choice = numpy.random.randint(1, 4)
	doors.remove(choice)

	# Two cases:
	# The car wasn't chosen, so the car is behind one of the other doors
	# The car was chosen, thus the car is not left
	if car in doors:
		# The non-car must be removed, switching will result in a win here
		doors = [car]
	else:
		# Randomly pick a door to remove, switching will result in a loss here
		index_to_remove = numpy.random.randint(0, 2)
		del doors[index_to_remove]
	# Switch to the other door
	choice = doors[0]
	# Add a win if the car and choice are the same.
	wins += 1 if car == choice else 0
print("Switching to the car resulted in {} wins out of 10000 for a win-rate of {}%.".format(wins, round(wins / 100, 2)))