from typing import List, Optional


class Seat:
    """A single seat in the open space that can be free or occupied by one person."""

    def __init__(self, free: bool = True, occupant: str = "") -> None:
        """
        Initialise a seat.

        :param free: Whether the seat is available (True by default).
        :param occupant: The name of the person sitting on the seat ("" if free).
        """
        self.free = free
        self.occupant = occupant

    def set_occupant(self, name: str) -> bool:
        """
        Assign a person to the seat if it is free.

        :param name: The name of the person to seat.
        :return: True if the person was seated, False if the seat was already taken.
        """
        if not self.free:
            return False
        self.occupant = name
        self.free = False
        return True

    def remove_occupant(self) -> str:
        """
        Free the seat and return the name of the person who was sitting there.

        :return: The name of the previous occupant ("" if the seat was already free).
        """
        previous = self.occupant
        self.occupant = ""
        self.free = True
        return previous

    def __str__(self) -> str:
        """
        Return a readable description of the seat.

        :return: The occupant's name, or "Empty" when the seat is free.
        """
        return self.occupant if not self.free else "Empty"


class Table:
    """A table made of a fixed number of seats."""

    def __init__(self, capacity: int = 4, seats: Optional[List[Seat]] = None) -> None:
        """
        Initialise a table with a given number of seats.

        :param capacity: The number of seats at the table (4 by default).
        :param seats: An optional pre-built list of Seat objects. When omitted,
                      `capacity` fresh free seats are created.
        """
        self.capacity = capacity
        if seats is None:
            self.seats = [Seat() for _ in range(capacity)]
        else:
            self.seats = seats

    def has_free_spot(self) -> bool:
        """
        Tell whether at least one seat is still available at the table.

        :return: True if a free seat exists, False otherwise.
        """
        return any(seat.free for seat in self.seats)

    def assign_seat(self, name: str) -> bool:
        """
        Seat a person on the first free seat found at the table.

        :param name: The name of the person to seat.
        :return: True if the person was seated, False if the table was full.
        """
        for seat in self.seats:
            if seat.free:
                return seat.set_occupant(name)
        return False

    def left_capacity(self) -> int:
        """
        Count how many seats are still free at the table.

        :return: The number of free seats.
        """
        return sum(seat.free for seat in self.seats)

    def __str__(self) -> str:
        """
        Return a readable, multi-line description of the table and its occupants.

        :return: A string listing each seat of the table.
        """
        lines = [f"  - {seat}" for seat in self.seats]
        return "\n".join(lines)
