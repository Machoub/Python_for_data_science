from abc import ABC, abstractmethod
from S1E9 import Character

class Baratheon(Character):
	"""CLASS BARATHEON"""
	def __init__(self, first_name: str, is_alive: bool = True, family_name: str = "Baratheon", eyes: str = "brown", hairs: str = "black"):
		"""Initialize a Baratheon character."""
		super().__init__(first_name, is_alive)
		self.family_name = family_name
		self.eyes = eyes
		self.hairs = hairs

	def __str__(self):
		"""Return a string representation of the Baratheon character."""
		return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

	def __repr__(self):
		"""Return a detailed string representation of the Baratheon character."""
		return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
	"""CLASS LANNISTER"""
	def __init__(self, first_name: str, is_alive: bool = True, family_name: str = "Lannister", eyes: str = "blue", hairs: str = "light"):
		"""Initialize a Lannister character."""
		super().__init__(first_name, is_alive)
		self.family_name = family_name
		self.eyes = eyes
		self.hairs = hairs
	
	def __str__(self):
		"""Return a string representation of the Lannister character."""
		return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

	def __repr__(self):
		"""Return a detailed string representation of the Lannister character."""
		return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
	
	def create_lannister(first_name: str, is_alive: bool = True):
		"""Create a Lannister character."""
		return Lannister(first_name, is_alive)

