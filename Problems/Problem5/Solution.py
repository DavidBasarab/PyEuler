def execute():
	print('5 Smallest multiple')

	index = 12
	max_check_number = 20

	def evenly_divided(number):
		start_item = 3

		while start_item <= max_check_number:
			if number % start_item != 0:
				return False
			start_item += 1

		return True

	while index > 0:
		if evenly_divided(index):
			print(f'Lowest Evenly divided is {index}')

			break
		index += 2

