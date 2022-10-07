"""Module iterate trough input file with numeric line strings"""


class NumericFileIteration:
    """Iterate trough input file with numeric line strings"""

    def __init__(self, path: str):
        with open(f"{path}", encoding="utf-8") as file:
            self.file_lines = [lines.rstrip("\n") for lines in file]
            file.close()

    def two_digits_multiplication(self):
        """1.a iteration for 2 digits sum 2020 and its multi multiplication"""
        for first in self.file_lines:
            for second in self.file_lines:
                if int(first) + int(second) == 2020:
                    return f"{first} * {second} = {int(first) * int(second)}"
        return None

    def three_digits_multiplication(self):
        """1.b iteration for 3 digits sum 2020 and its multi multiplication"""

        for first in self.file_lines:
            for second in self.file_lines:
                for third in self.file_lines:
                    if int(first) + int(second) + int(third) == 2020:
                        return (
                            f"{first} * {second}: * {third} = "
                            f"{int(first) * int(second) * int(third)}"
                        )
        return None
