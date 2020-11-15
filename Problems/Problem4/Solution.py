def execute():
	print('Problem 4 Largest palindrome product')

	def is_palindrome(number):
		forward = str(number)
		backwards = ""

		index = len(forward) - 1

		while index >= 0:
			backwards += forward[index]
			index -= 1

		return forward == backwards

	max_number = 999

	first_index = max_number
	second_index = max_number
	max_first_digit = 0
	max_second_digit = 0

	max_palindrome = 0

	while first_index >= 1:
		while second_index >= 1:
			product = first_index * second_index
			if is_palindrome(product) and product > max_palindrome:
				max_palindrome = product
				max_first_digit = first_index
				max_second_digit = second_index
			second_index -= 1
		first_index -= 1
		second_index = max_number

	print(f'Max Palindrome for {max_number} is {max_palindrome} = {max_first_digit} x {max_second_digit}')
