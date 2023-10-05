from collections import namedtuple
from typing import Dict

from constants import GRID_SIZE
from objects.coordinate import Coord
from utils.calculate_stuff import map_to_area_coord


class Board:
    def __init__(self, rows=None, cols=None, areas=None):
        if rows is None or cols is None or areas is None:
            self.rows = {i: [0 for i in range(GRID_SIZE)] for i in range(GRID_SIZE)}
            self.cols = {i: [0 for i in range(GRID_SIZE)] for i in range(GRID_SIZE)}
            self.areas = {i: [0 for i in range(GRID_SIZE)] for i in range(GRID_SIZE)}
        else:
            self.rows = rows
            self.rows = cols
            self.areas = areas

        self.fixed_values: Dict[Coord, int] = {}

    def print(self):
        print("Rows: ")
        for row in self.rows:
            print(f'{row}: {self.rows[row]}')
        print("Cols: ")
        for col in self.cols:
            print(f'{col}: {self.cols[col]}')
        print("Areas: ")
        for area in self.areas:
            print(f'{area}: {self.areas[area]}')
        print("Fixed values: ")
        for coord in self.fixed_values:
            print(f'{coord}: {self.fixed_values[coord]}')

    def add_value_by_coord(self, coord: Coord, value: int):
        self.rows[coord.row][coord.col] = value
        self.cols[coord.col][coord.row] = value
        area_index, value_index = map_to_area_coord(coord)
        self.areas[area_index][value_index] = value
        self.fixed_values[coord] = value