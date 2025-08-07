from abc import ABC, abstractmethod

class Character(ABC):
		"""CLASS CHARACTER"""
		@abstractmethod
		def __init__(self, first_name: str, is_alive: bool = True):
			self.first_name = first_name
			self.is_alive = is_alive
		
		def die(self):
			"""Set the character's status to dead."""
			self.is_alive = False

class Stark(Character):
		"""CLASS STARK"""
		def __init__(self, first_name: str, is_alive: bool = True):
			"""Initialize a Stark character."""
			super().__init__(first_name, is_alive)
