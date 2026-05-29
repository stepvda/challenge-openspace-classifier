from typing import List


def read_names(filepath: str) -> List[str]:
    """
    Read a list of colleague names from a plain text file (one name per line).

    :param filepath: The path to the .txt file containing one name per line.
    :return: A list of names (empty lines are ignored and whitespace is stripped).
    """
    names: List[str] = []
    # Open the file and read it line by line so the file is closed automatically.
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            # Remove surrounding whitespace and the trailing newline.
            name = line.strip()
            # Skip blank lines to avoid creating empty occupants.
            if name:
                names.append(name)
    return names
