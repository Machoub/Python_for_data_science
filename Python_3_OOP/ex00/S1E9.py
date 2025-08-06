from abc import ABC, abstractmethod

class character(ABC):
		"""CLASS CHARACTER"""
		@abstractmethod
		def __init__(self, first_name: str, is_alive: bool = True):
			self.first_name = first_name
			self.is_alive = is_alive

class Stark(character):
		"""CLASS STARK"""
		def __init__(self, first_name: str, is_alive: bool = True):
			super().__init__(first_name, is_alive)

		def die(self):
			self.is_alive = False

def main():
	Ned = Stark("Ned")
	print(Ned.__dict__)
	print(Ned.is_alive)
	Ned.die()
	print(Ned.is_alive)
	print(Ned.__doc__)
	print(Ned.__init__.__doc__)
	print(Ned.die.__doc__)
	print("---")
	Lyanna = Stark("Lyanna", False)
	print(Lyanna.__dict__)


if __name__ == "__main__":
	main()