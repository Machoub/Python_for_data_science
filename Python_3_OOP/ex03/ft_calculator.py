class calculator:
	def __init__(self, num: list[float]):
		self.num = num
	
	def __repr__(self):
		return f"{self.num}"

	def __add__(self, other) -> list[float]:
		return (calculator([x + other for x in self.num]))

	def __sub__(self, other) -> list[float]:
		return (calculator([x - other for x in self.num]))

	def __mul__(self, other) -> list[float]:
		return (calculator([x * other for x in self.num]))

	def __truediv__(self, other) -> list[float]:
		if other == 0:
			raise ValueError("Cannot divide by zero.")
		return (calculator([x / other for x in self.num]))

def main():
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    print(v1 + 5)
    print("---")

    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    print(v2 * 5)
    print("---")

    v3 = calculator([10.0, 15.0, 20.0])
    resultat = v3 - 5
    print(resultat)       # [5.0, 10.0, 15.0]
    print(resultat / 5)   # [1.0, 2.0, 3.0]

if __name__ == "__main__":
	main()