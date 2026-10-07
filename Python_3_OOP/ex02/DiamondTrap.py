from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """CLASS KING"""

    def __init__(self, first_name: str, is_alive: bool = True,
                 family_name: str = "Baratheon", eyes: str = "brown",
                 hairs: str = "dark"):
        """Initialize a King character."""
        super().__init__(first_name, is_alive, family_name, eyes, hairs)

    @property
    def property_eyes(self):
        """Eye color of the King."""
        return self.eyes

    @property_eyes.setter
    def property_eyes(self, value):
        """Set the eye color of the King."""
        self.eyes = value

    def get_eyes(self):
        """Get the eye color of the King."""
        return self.property_eyes

    def set_eyes(self, eyes):
        """Set the eye color of the King."""
        self.property_eyes = eyes

    @property
    def property_hairs(self):
        """Hair color of the King."""
        return self.hairs

    @property_hairs.setter
    def property_hairs(self, value):
        """Set the hair color of the King."""
        self.hairs = value

    def get_hairs(self):
        """Get the hair color of the King."""
        return self.property_hairs

    def set_hairs(self, hairs):
        """Set the hair color of the King."""
        self.property_hairs = hairs
