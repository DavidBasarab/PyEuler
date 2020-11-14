def execute():
	print('Problem 3 Largest prime factor')

	is_prime = lambda number: all(number % i != 0 for i in range(2, int(number ** .5) + 1))

	def prime_series(max_number):
		primes = []
		for index in range(2, max_number):
			if is_prime(index):
				primes.append(index)
			else:
				pass

		return primes

	prime_numbers = prime_series(13195)

	def find_prime_factors(number):
		if is_prime(number):
			return [number]

		factors = []

		for current_prime in prime_numbers:
			if number % current_prime == 0:
				factors.append(current_prime)
				next_number = int(number / current_prime)
				factors = factors + find_prime_factors(next_number)
				break

		return factors

	prime_factors = find_prime_factors(600851475143)

	print(prime_factors)

	print(f'Largest Prime Number of 600851475143 is {prime_factors[-1]}')

	print('')


