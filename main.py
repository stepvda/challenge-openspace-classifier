import sys
from typing import List

from utils.file_utils import read_names
from utils.openspace import Openspace

# Default open space setup: 6 tables of 4 seats = 24 seats.
DEFAULT_NUMBER_OF_TABLES = 6
DEFAULT_SEATS_PER_TABLE = 4

# Default location of the colleagues file and of the saved arrangement.
DEFAULT_COLLEAGUES_FILE = "colleagues.txt"
OUTPUT_FILE = "openspace_arrangement.txt"


def main() -> None:
    """
    Load the colleagues, randomly seat them in the open space, then display and
    save the result.

    The colleagues file path can be passed as the first command line argument,
    otherwise the default file is used.

    :return: None.
    """
    # Use the path given on the command line if any, otherwise the default file.
    filepath = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_COLLEAGUES_FILE

    # Load the colleagues from the text file.
    names: List[str] = read_names(filepath)
    print(f"Loaded {len(names)} colleagues from '{filepath}'.\n")

    # Build the open space with the default setup and seat everyone randomly.
    openspace = Openspace(
        number_of_tables=DEFAULT_NUMBER_OF_TABLES,
        seats_per_table=DEFAULT_SEATS_PER_TABLE,
    )
    not_seated = openspace.organize(names)

    # Show the resulting arrangement and the remaining capacity.
    openspace.display()

    # Warn the user if there were more people than available seats.
    if not_seated:
        print(
            f"\nWarning: {len(not_seated)} people could not be seated "
            f"(not enough seats): {', '.join(not_seated)}"
        )

    # Save the arrangement to a file so it can be shared.
    openspace.store(OUTPUT_FILE)
    print(f"\nArrangement saved to '{OUTPUT_FILE}'.")


if __name__ == "__main__":
    main()
