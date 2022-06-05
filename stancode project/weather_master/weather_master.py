"""
File: weather_master.py
Name:Jan Guo
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
# This constant controls when to stop
EXIT = -100


def main():
	"""
	This program finds the highest/lowest temperature, average temperature and cold days among user inputs.
	"""
	print("standCode \"Weather Master 4.0\"!")
	temperature = int(input('Next Temperature: (or '+str(EXIT)+' to quit)?'))
	if temperature == EXIT:
		print('No temperatures were entered.')
	else:
		# Define a variable to find the highest temperature among inputs
		highest = temperature
		# Define a variable to find the lowest temperature among inputs
		lowest = temperature
		# Define a variable to calculate how many temperatures that were entered
		counts = 1
		# Define a variable to calculate the total amount of temperatures that were entered
		total = temperature
		# Define a variable to calculate how many cold days
		if temperature < 16:
			cold_day = 1
		else:
			cold_day = 0
		while True:
			temperature = int(input('Next Temperature: (or '+str(EXIT)+' to quit)?'))
			if temperature == EXIT:
				break
			else:
				counts += 1
				total = total + temperature
				if temperature < 16:
					cold_day += 1
			if highest < temperature:
				highest = temperature
			if lowest > temperature:
				lowest = temperature
		# Calculate average temperature
		avg = float(total/counts)
		print('Highest temperature='+str(highest))
		print('Lowest temperature=' + str(lowest))
		print('Average='+str(avg))
		print(str(cold_day)+" "+'cold day(s)')









###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
