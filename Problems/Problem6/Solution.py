def execute():
	print('6 Sum square difference')

	max_number = 100
	sum_of_squares = 0
	sum_of_number = 0

	current_number = 0

	while current_number <= max_number:
		sum_of_squares += (current_number * current_number)
		sum_of_number += current_number
		current_number += 1

	square_of_sum = sum_of_number * sum_of_number

	difference = square_of_sum - sum_of_squares

	print(f'Difference of {square_of_sum} - {sum_of_squares} = {difference}')