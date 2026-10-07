class calculator:
    """Compute dot product, addition and subtraction of two vectors."""

    def __init__(self, num: list):
        """Store the list of numbers to work on."""
        self.num = num

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Print the dot product of two vectors."""
        res = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {res}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Print the element-wise sum of two vectors."""
        res = list(float(x) + float(y) for x, y in zip(V1, V2))
        print(f"Add Vector is : {res}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Print the element-wise difference of two vectors."""
        res = list(float(x) - float(y) for x, y in zip(V1, V2))
        print(f"Sous Vector is: {res}")
