"""Module iterate trough input file with  line strings"""


class StringFileIteration:
    """Iterate trough input file with line strings"""

    def __init__(self, path: str):
        with open(f"{path}", encoding="utf-8") as file:
            self.file_lines = [lines.rstrip("\n") for lines in file]
            file.close()

    def valid_strings(self):
        """Count valid strings"""
        return len(
            set(
                values for values in self.file_lines
                if values.replace(":", "").split(" ")[1] in values.split(" ")[2]
            )
        )

    def valid_strings_in_positions(self):
        """Count valid strings and position"""
        return len(
            set(
                values for values in self.file_lines
                if (
                        values.replace(":", "").split(" ")[1]
                        in [*values.split(" ")[2]][
                            int(str(values.split(" ")[0]).split("-", maxsplit=1)[0]) - 1
                            ]
                        not in [*values.split(" ")[2]][
                            int(str(values.split(" ")[0]).split("-")[1]) - 1
                            ]
                        and [*values.split(" ")[2]][
                            int(str(values.split(" ")[0]).split("-", maxsplit=1)[0]) - 1
                            ]
                )
            )
        )


print(StringFileIteration("input/input2.txt").valid_strings())
print(StringFileIteration("input/input2.txt").valid_strings_in_positions())
