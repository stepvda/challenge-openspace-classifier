# Table of Contents

* [main](#main)
  * [main](#main.main)
* [utils.file\_utils](#utils.file_utils)
  * [read\_names](#utils.file_utils.read_names)
* [utils.table](#utils.table)
  * [Seat](#utils.table.Seat)
    * [\_\_init\_\_](#utils.table.Seat.__init__)
    * [set\_occupant](#utils.table.Seat.set_occupant)
    * [remove\_occupant](#utils.table.Seat.remove_occupant)
    * [\_\_str\_\_](#utils.table.Seat.__str__)
  * [Table](#utils.table.Table)
    * [\_\_init\_\_](#utils.table.Table.__init__)
    * [has\_free\_spot](#utils.table.Table.has_free_spot)
    * [assign\_seat](#utils.table.Table.assign_seat)
    * [left\_capacity](#utils.table.Table.left_capacity)
    * [\_\_str\_\_](#utils.table.Table.__str__)
* [utils.openspace](#utils.openspace)
  * [Openspace](#utils.openspace.Openspace)
    * [\_\_init\_\_](#utils.openspace.Openspace.__init__)
    * [organize](#utils.openspace.Openspace.organize)
    * [number\_of\_seats](#utils.openspace.Openspace.number_of_seats)
    * [seats\_left](#utils.openspace.Openspace.seats_left)
    * [display](#utils.openspace.Openspace.display)
    * [store](#utils.openspace.Openspace.store)
    * [\_\_str\_\_](#utils.openspace.Openspace.__str__)

<a id="main"></a>

# main

<a id="main.main"></a>

#### main

```python
def main() -> None
```

Load the colleagues, randomly seat them in the open space, then display and

save the result.

The colleagues file path can be passed as the first command line argument,
otherwise the default file is used.

**Returns**:

None.

<a id="utils.file_utils"></a>

# utils.file\_utils

<a id="utils.file_utils.read_names"></a>

#### read\_names

```python
def read_names(filepath: str) -> List[str]
```

Read a list of colleague names from a plain text file (one name per line).

**Arguments**:

- `filepath`: The path to the .txt file containing one name per line.

**Returns**:

A list of names (empty lines are ignored and whitespace is stripped).

<a id="utils.table"></a>

# utils.table

<a id="utils.table.Seat"></a>

## Seat Objects

```python
class Seat()
```

A single seat in the open space that can be free or occupied by one person.

<a id="utils.table.Seat.__init__"></a>

#### \_\_init\_\_

```python
def __init__(free: bool = True, occupant: str = "") -> None
```

Initialise a seat.

**Arguments**:

- `free`: Whether the seat is available (True by default).
- `occupant`: The name of the person sitting on the seat ("" if free).

<a id="utils.table.Seat.set_occupant"></a>

#### set\_occupant

```python
def set_occupant(name: str) -> bool
```

Assign a person to the seat if it is free.

**Arguments**:

- `name`: The name of the person to seat.

**Returns**:

True if the person was seated, False if the seat was already taken.

<a id="utils.table.Seat.remove_occupant"></a>

#### remove\_occupant

```python
def remove_occupant() -> str
```

Free the seat and return the name of the person who was sitting there.

**Returns**:

The name of the previous occupant ("" if the seat was already free).

<a id="utils.table.Seat.__str__"></a>

#### \_\_str\_\_

```python
def __str__() -> str
```

Return a readable description of the seat.

**Returns**:

The occupant's name, or "Empty" when the seat is free.

<a id="utils.table.Table"></a>

## Table Objects

```python
class Table()
```

A table made of a fixed number of seats.

<a id="utils.table.Table.__init__"></a>

#### \_\_init\_\_

```python
def __init__(capacity: int = 4, seats: Optional[List[Seat]] = None) -> None
```

Initialise a table with a given number of seats.

**Arguments**:

- `capacity`: The number of seats at the table (4 by default).
- `seats`: An optional pre-built list of Seat objects. When omitted,
`capacity` fresh free seats are created.

<a id="utils.table.Table.has_free_spot"></a>

#### has\_free\_spot

```python
def has_free_spot() -> bool
```

Tell whether at least one seat is still available at the table.

**Returns**:

True if a free seat exists, False otherwise.

<a id="utils.table.Table.assign_seat"></a>

#### assign\_seat

```python
def assign_seat(name: str) -> bool
```

Seat a person on the first free seat found at the table.

**Arguments**:

- `name`: The name of the person to seat.

**Returns**:

True if the person was seated, False if the table was full.

<a id="utils.table.Table.left_capacity"></a>

#### left\_capacity

```python
def left_capacity() -> int
```

Count how many seats are still free at the table.

**Returns**:

The number of free seats.

<a id="utils.table.Table.__str__"></a>

#### \_\_str\_\_

```python
def __str__() -> str
```

Return a readable, multi-line description of the table and its occupants.

**Returns**:

A string listing each seat of the table.

<a id="utils.openspace"></a>

# utils.openspace

<a id="utils.openspace.Openspace"></a>

## Openspace Objects

```python
class Openspace()
```

An open space made of several tables onto which people are seated randomly.

<a id="utils.openspace.Openspace.__init__"></a>

#### \_\_init\_\_

```python
def __init__(tables: Optional[List[Table]] = None,
             number_of_tables: int = 6,
             seats_per_table: int = 4) -> None
```

Initialise the open space.

**Arguments**:

- `tables`: An optional pre-built list of Table objects. When omitted,
`number_of_tables` tables of `seats_per_table` seats are created.
- `number_of_tables`: The number of tables to build (6 by default).
- `seats_per_table`: The number of seats per table (4 by default).

<a id="utils.openspace.Openspace.organize"></a>

#### organize

```python
def organize(names: List[str]) -> List[str]
```

Randomly assign the given people to the seats of the open space.

All seats from every table are gathered, shuffled, and then filled one by
one. If there are more people than seats, the surplus people are returned
so the caller can report them.

**Arguments**:

- `names`: The list of names to seat in the open space.

**Returns**:

The list of people who could not be seated (empty if everyone fit).

<a id="utils.openspace.Openspace.number_of_seats"></a>

#### number\_of\_seats

```python
def number_of_seats() -> int
```

Count the total number of seats in the open space.

**Returns**:

The total seat count across all tables.

<a id="utils.openspace.Openspace.seats_left"></a>

#### seats\_left

```python
def seats_left() -> int
```

Count how many seats are still free across the whole open space.

**Returns**:

The number of free seats.

<a id="utils.openspace.Openspace.display"></a>

#### display

```python
def display() -> None
```

Print every table and its occupants in a readable way.

**Returns**:

None.

<a id="utils.openspace.Openspace.store"></a>

#### store

```python
def store(filename: str) -> None
```

Save the current seating arrangement to a text file.

**Arguments**:

- `filename`: The path of the file to write the arrangement to.

**Returns**:

None.

<a id="utils.openspace.Openspace.__str__"></a>

#### \_\_str\_\_

```python
def __str__() -> str
```

Return a readable, multi-line description of the whole open space.

**Returns**:

A string listing every table and its occupants.

