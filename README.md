# Open Space Organizer

A small Python program that **randomly assigns colleagues to seats** in an open
space. Our company moved to a new office — an open space with **12** **tables of 4
seats (24 seats)** — and we want to change seats every day to get to know each
other better.

## Description

The program:

- Loads a list of colleagues from a `.txt` file (one name per line).
- Randomly distributes the people across the tables of the open space.
- Reports how many seats are left.
- Handles the case where there are **more people than seats**.
- Displays the result nicely and saves it to a file.

It is built with **Object-Oriented Programming** around three classes:

| Class         | File                   | Responsibility                                  |
| ------------- | ---------------------- | ----------------------------------------------- |
| `Seat`      | `utils/table.py`     | A single seat (free or occupied).               |
| `Table`     | `utils/table.py`     | A table made of several seats.                  |
| `Openspace` | `utils/openspace.py` | The whole room: organizes, displays and stores. |

## Project structure

```
challenge-openspace-classifier/
├── main.py                 # Entry point: loads, organizes and displays
├── colleagues.txt          # Sample list of colleagues (one name per line)
├── notebook_guide.ipynb    # Notebook used to prototype the logic
├── README.md
└── utils/
    ├── file_utils.py       # Reads the names from a .txt file
    ├── table.py            # Seat and Table classes
    └── openspace.py        # Openspace class
```

## Installation

This project uses only the Python standard library, so there is nothing to
install beyond **Python 3.8+**.

```bash
git clone https://github.com/<your-username>/challenge-openspace-classifier.git
cd challenge-openspace-classifier
```

## Usage

Run the program with the default colleagues file (`colleagues.txt`):

```bash
python main.py
```

Or provide your own list of colleagues as an argument:

```bash
python main.py path/to/your_colleagues.txt
```

The arrangement is printed to the terminal and saved to
`openspace_arrangement.txt`.

### Example output

```
Loaded 24 colleagues from 'colleagues.txt'.

Table 1:
  - Max
  - Anna
  - Imad
  - Thi
...
Seats left: 0 / 24

Arrangement saved to 'openspace_arrangement.txt'.
```
