def ft_statistics(*args: any, **kwargs: any)-> None:
	for key, value in kwargs.items():
		if not isinstance(value, str):
			print(f"Invalid statistic type for {key}: {type(value)}")
			return
		if args is None or len(args) == 0:
			print("ERROR")
		else:
			if value == "mean":
				print(f'{value}: {sum(args) / len(args) if args else 0}')
			elif value == "median":
				mediane = sorted(args)[len(args) // 2] if args else 0
				print(f'{value}: {mediane}')
			elif value == "quartile":
				sorted_args = sorted(args)
				q1 = float(sorted_args[len(sorted_args) // 4]) if len(sorted_args) > 0 else 0
				q3 = float(sorted_args[3 * len(sorted_args) // 4]) if len(sorted_args) > 0 else 0
				print(f'{value}: Quartiles: [{q1}, {q3}]')
			elif value == "var":
				mean = sum(args) / len(args) if args else 0
				var = sum((xi - mean) ** 2 for xi in args) / len(args) if args else 0
				print(f'{value}: {var}')
			elif value == "std":
				mean = sum(args) / len(args) if args else 0
				stddev = (sum((xi - mean) ** 2 for xi in args) / len(args)) ** 0.5 if args else 0
				print(f'{value}: {stddev}')



if __name__ == "__main__":
	ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
	print("-----")
	ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
	print("-----")
	ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
	print("-----")
	ft_statistics(toto="mean", tutu="median", tata="quartile")