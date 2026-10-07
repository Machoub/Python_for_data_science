import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Return a random identifier made of 15 lowercase letters."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A student with a name, a surname, a login and a random id."""

    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """Build the login from the name and the surname."""
        self.login = self.name[0].upper() + self.surname.lower()


def main():
    """Create a student and print it."""
    try:
        student = Student(name="Edward", surname="agle")
        print(student)
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()
