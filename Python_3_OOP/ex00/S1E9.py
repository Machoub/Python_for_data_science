from abc import ABC, abstractmethod

class Character(ABC):
		"""CLASS CHARACTER"""
		@abstractmethod
		def __init__(self, first_name: str, is_alive: bool = True):
			self.first_name = first_name
			self.is_alive = is_alive

class Stark(Character):
		"""CLASS STARK"""
		def __init__(self, first_name: str, is_alive: bool = True):
			"""Initialize a Stark character."""
			super().__init__(first_name, is_alive)

		def die(self):
			"""Set the character's status to dead."""
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
	try:
		hodor = Character("hodor")
	except TypeError as e:
		print(e)


if __name__ == "__main__":
	main()