import random
from typing import List, Optional

from utils.table import Seat, Table


class Openspace:
    """An open space made of several tables onto which people are seated randomly."""

    def __init__(
        self,
        tables: Optional[List[Table]] = None,
        number_of_tables: int = 6,
        seats_per_table: int = 4,
    ) -> None:
        """
        Initialise the open space.

        :param tables: An optional pre-built list of Table objects. When omitted,
                       `number_of_tables` tables of `seats_per_table` seats are created.
        :param number_of_tables: The number of tables to build (6 by default).
        :param seats_per_table: The number of seats per table (4 by default).
        """
        if tables is None:
            self.tables = [Table(seats_per_table) for _ in range(number_of_tables)]
        else:
            self.tables = tables
        self.number_of_tables = len(self.tables)

    def organize(self, names: List[str]) -> List[str]:
        """
        Randomly assign the given people to the seats of the open space.

        All seats from every table are gathered, shuffled, and then filled one by
        one. If there are more people than seats, the surplus people are returned
        so the caller can report them.

        :param names: The list of names to seat in the open space.
        :return: The list of people who could not be seated (empty if everyone fit).
        """
        # Gather every seat of every table into a single flat list.
        seats: List[Seat] = []
        for table in self.tables:
            seats.extend(table.seats)

        # Shuffle the seats so the assignment is random.
        random.shuffle(seats)

        # Seat as many people as there are available seats.
        not_seated: List[str] = []
        for index, name in enumerate(names):
            if index < len(seats):
                seats[index].set_occupant(name)
            else:
                # No seat left for this person: remember them for the report.
                not_seated.append(name)

        return not_seated

    def number_of_seats(self) -> int:
        """
        Count the total number of seats in the open space.

        :return: The total seat count across all tables.
        """
        return sum(len(table.seats) for table in self.tables)

    def seats_left(self) -> int:
        """
        Count how many seats are still free across the whole open space.

        :return: The number of free seats.
        """
        return sum(table.left_capacity() for table in self.tables)

    def display(self) -> None:
        """
        Print every table and its occupants in a readable way.

        :return: None.
        """
        for index, table in enumerate(self.tables):
            print(f"Table {index + 1}:")
            print(table)
        print(f"\nSeats left: {self.seats_left()} / {self.number_of_seats()}")

    def store(self, filename: str) -> None:
        """
        Save the current seating arrangement to a text file.

        :param filename: The path of the file to write the arrangement to.
        :return: None.
        """
        with open(filename, "w", encoding="utf-8") as file:
            for index, table in enumerate(self.tables):
                file.write(f"Table {index + 1}:\n")
                file.write(f"{table}\n")
            file.write(f"\nSeats left: {self.seats_left()} / {self.number_of_seats()}\n")

    def __str__(self) -> str:
        """
        Return a readable, multi-line description of the whole open space.

        :return: A string listing every table and its occupants.
        """
        blocks = []
        for index, table in enumerate(self.tables):
            blocks.append(f"Table {index + 1}:\n{table}")
        blocks.append(f"\nSeats left: {self.seats_left()} / {self.number_of_seats()}")
        return "\n".join(blocks)
