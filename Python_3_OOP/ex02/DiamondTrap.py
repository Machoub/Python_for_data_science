from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
	"""CLASS KING"""
	def __init__(self, first_name: str, is_alive: bool = True, family_name: str = "Baratheon", eyes: str = "brown", hairs: str = "dark"):
		"""Initialize a King character."""
		super().__init__(first_name, is_alive, family_name, eyes, hairs)

	def set_eyes(self, eyes: str):
		"""Set the eye color of the King."""
		self.eyes = eyes
	def get_eyes(self) -> str:
		"""Get the eye color of the King."""
		return self.eyes
	
	def set_hairs(self, hairs: str):
		"""Set the hair color of the King."""
		self.hairs = hairs
	def get_hairs(self) -> str:
		"""Get the hair color of the King."""
		return self.hairs

def main():
	Joffrey = King("Joffrey")
	print(Joffrey.__dict__)
	Joffrey.set_eyes("blue")
	Joffrey.set_hairs("light")
	print(Joffrey.get_eyes())
	print(Joffrey.get_hairs())
	print(Joffrey.__dict__)


if __name__ == "__main__":
	main()