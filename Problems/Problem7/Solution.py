def execute():
	print('7 10001st prime')

	for num in range(1, 10002):
		for i in range(2, num):
			if num % i == 0:
				break
		else:
			print(num, 'is a prime number')
