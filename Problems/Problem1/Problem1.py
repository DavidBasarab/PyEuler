def execute():
	print('Problem 1 Multiples of 3 and 5')
	mode_value = 6 % 4
	print(f'This is the value of 6 % 4 <{mode_value}>')

	valid_numbers = []

	index = 1
	stop_number = 1000

	while index < stop_number:
		if index % 3 == 0 or index % 5 == 0:
			valid_numbers.append(index)
		index += 1

	total = 0

	for n in valid_numbers:
		total += n

	print(f'Total less than {stop_number} is {total}')