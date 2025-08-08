def square(x: int | float)-> int | float:
	if isinstance(x, (int, float)):
		return x ** 2
	else:
		raise TypeError("Input must be an int or float")
	
def pow(x: int | float)-> int | float:
	if isinstance(x, (int, float)):
		return x ** x
	else:
		raise TypeError("Input must be an int or float")

def outer(x: int | float, function)-> object:
	count = 0
	def inner()-> float:
		nonlocal x
		x = function(x)
		return x
	return inner

def main():
	my_counter = outer(3, square)
	print(my_counter())
	print(my_counter())
	print(my_counter())
	print("---")
	another_counter = outer(1.5, pow)
	print(another_counter())
	print(another_counter())
	print(another_counter())

if __name__ == "__main__":
	main()