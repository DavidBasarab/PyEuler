def execute():
	print('Problem 3 Largest prime factor')

	is_prime = lambda number: all(number % i != 0 for i in range(2, int(number ** .5) + 1))

	def prime_series(max_number):
		print(f'Going to list all primes to {max_number}')
		for index in range(2, max_number):
			if is_prime(index):
				print(index, end=" ")
			else:
				pass

	range_number = int(input("Enter the input Range :"))

	prime_series(range_number)

	print('')


