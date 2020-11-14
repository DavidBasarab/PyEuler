is_prime = lambda number: all(number % i != 0 for i in range(2, int(number ** .5) + 1))

def prime_series(max_number):
	primes = []
	for index in range(2, max_number):
		if is_prime(index):
			primes.append(index)
		else:
			pass

	return primes