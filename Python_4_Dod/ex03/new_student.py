import random
import string
from dataclasses import dataclass, field

def generate_id()-> str:
	return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
		name: str = field(init=True)
		surname: str = field(init=True)
		active: bool = field(default=True)
		login: str = field(init=False)
		id: str = field(init=False,default_factory=generate_id)

		def __post_init__(self):
			self.login = self.name[0].upper() + self.surname.lower()

def main():
	try:
		student = Student(name = "Edward", surname = "agle")
		print(student)
		studenté = Student(name = "Edward", surname = "agle", id = "toto")
		print(studenté)
	except TypeError as e:
		print(e)

if __name__ == "__main__":
	main()