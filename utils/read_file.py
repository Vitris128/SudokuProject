from objects.board import Board
from objects.coordinate import Coord


def read_from_file(file_path: str):
    board = Board()
    with open(file_path, "r") as file:
        for row, line in enumerate(file):
            curr_row = [int(x) for x in line.split()]
            for col, value in enumerate(curr_row):
                coord = Coord(row, col)
                if value != 0:
                    board.add_value_by_coord(coord, value)
    return board



