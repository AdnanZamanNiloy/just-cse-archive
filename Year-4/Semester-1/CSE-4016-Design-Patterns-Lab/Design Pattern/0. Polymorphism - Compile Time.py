class clsCalculator:
    def __init__(self):
        self.nResult = 0

    def add(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            self.nResult = a + b
        elif isinstance(a, float) and isinstance(b, float):
            self.nResult = a + b + 5
        else:
            raise TypeError("Unsupported data types")

        return self.nResult


# Main Function
oCalculator = clsCalculator()

print(oCalculator.add(5, 5))

print(oCalculator.add(5.0, 5.0))