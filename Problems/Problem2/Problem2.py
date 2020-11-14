def execute():
	print('Problem 2 Even Fibonacci numbers')
	fibonacci_numbers = [1, 2]
	even_fibonacci_numbers = [2]

	keep_going = True
	index = 2
	max_value = 4000001

	while keep_going:
		first_term = fibonacci_numbers[index - 2]
		second_term = fibonacci_numbers[index - 1]
		next_term = first_term + second_term

		if next_term > max_value:
			break

		fibonacci_numbers.append(next_term)

		if next_term % 2 == 0:
			print(f'Adding term <{next_term}>')
			even_fibonacci_numbers.append(next_term)

		index += 1

	sum = 0

	for n in even_fibonacci_numbers:
		sum += n

	print(f'Sum of Even Fibonacci Numbers with value less than {max_value} is < {sum} >')