class calculator:
    """Apply a scalar operation to every element of a list of numbers."""

    def __init__(self, num: list[float]):
        """Store the list of numbers to work on."""
        self.num = num

    def __add__(self, other) -> None:
        """Add a scalar to each element in place and print it."""
        self.num = [x + other for x in self.num]
        print(f"{self.num}")

    def __sub__(self, other) -> None:
        """Subtract a scalar from each element in place and print it."""
        self.num = [x - other for x in self.num]
        print(f"{self.num}")

    def __mul__(self, other) -> None:
        """Multiply each element by a scalar in place and print it."""
        self.num = [x * other for x in self.num]
        print(f"{self.num}")

    def __truediv__(self, other) -> None:
        """Divide each element by a scalar in place and print it.

        If the scalar is zero, an error message is printed instead and
        the vector is left unchanged.
        """
        try:
            if other == 0:
                raise ValueError("Cannot divide by zero.")
        except ValueError as e:
            print(e)
        else:
            self.num = [x / other for x in self.num]
            print(f"{self.num}")
