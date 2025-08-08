def callLimit(limit: int):
	count = 0
	def callLimiter(function): 
		def limit_function(*args: any, **kwds: any):
			try:
				nonlocal count
				count += 1
				if count <= limit:
					return function(*args, **kwds)
				else:
					raise AssertionError(f"{function} call too many times")
			except AssertionError as e:
				print(f"Error occurred: {e}")
		return limit_function
	return callLimiter

def main():
	@callLimit(3)
	def f():
		print("f()")

	@callLimit(1)
	def g():
		print("g()")

	for i in range(3):
		f()
		g()

if __name__ == "__main__":
	main()