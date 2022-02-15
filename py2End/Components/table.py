from __future__ import annotations
from component import *
from typing import Dict, Any, List, Tuple
from colorama import init, Fore
from utils import *

import gi
gi.require_version('Atspi', '2.0')
from gi.repository import Atspi

init()

class Table(E2eComponent):

    def __init__(self: Table, obj: Atspi.Object):
        super().__init__(obj)

    def check_data_table(self, data):
        check = 0
        print(Fore.WHITE + self.component.get_name())
        for i in range(self.get_rows_number()):
            row = self.get_row(i)
            for n in range(len(data)):
                if data[n] == row.get_value():
                    check = check + 1
                    print(Fore.GREEN + f"##### CHECK {check}/{len(data)} #####")
                    if check == len(data):
                        return True
        return False

    def select_row(self: Table, row: int):
        if self.get_rows_number() <= row:
            return False
        self.component.add_row_selection(row)
        return True

    def select_column(self: Table, column: int):
        if self.component.add_row_selection(column) is not True:
            print(Fore.RED + f"La tabla {self.name} no tiene columna {column}")
            return False
        return True

    def select(self: Table, type: int, n: int):
        if type == 0:
            self.select_row(n)
        elif type == 1:
            self.select_column(n)
        else:
            print(Fore.RED + "Error")

    def deselect_row(self: Table, row: int):
        if self.component.remove_row_selection(row) is not True:
            print(Fore.RED + f"La tabla {self.name} no tiene fila {row}")

    def deselect_column(self: Table, column: int):
        if self.component.remove_row_selection(column) is not True:
            print(Fore.RED + f"La tabla {self.name} no tiene columna {column}")

    def deselect(self: Table, type: int, n: int):
        if type == 0:
            self.deselect_row(n)
        elif type == 1:
            self.deselect_column(n)
        else:
            print(Fore.RED + "Error")

    def get_selected(self: Table, type: int, n: int):
        if type == 0:
            return self.component.get_selected_rows()
        elif type == 1:
            return self.component.get_selected_columns()
        else:
            print(Fore.RED + "Error")

    def __get_n_cells(self: Table):
        count = 0
        for cell in self.tree_walk(self.component):
            if cell.get_role_name() == "table cell" and cell.get_name() != "":
                count = count + 1
        return count

    def __get_columns_for_row(self: Table):
        cfr = self.__get_n_cells() / self.get_rows_number()
        return cfr

    def get_cell(self: Table, row: int, column: int):
        posfila = 0
        poscolumna = 0
        for dato in self.tree_walk(self.component):
            if dato.get_role_name() == "table cell" and dato.get_name() != "":
                if posfila == row and poscolumna == column:
                    cell = Cell(dato)
                    return cell
                poscolumna = poscolumna + 1
                if poscolumna == self.__get_columns_for_row():
                    posfila = posfila + 1
                    poscolumna = 0
        else:
            print("celda no encontrada")

    def get_columns_number(self: Table):
        return self.component.get_n_columns()

    def get_rows_number(self: Table):
        return self.component.get_n_rows()

    def get_selected_columns_number(self: Table):
        return self.component.get_n_selected_columns()

    def get_selected_rows_number(self: Table):
        return self.component.get_n_selected_rows()

    def get_column_header(self: Table, column: int):
        header = Cell(self.component.get_column_header(column))
        return header

    def get_column_name(self: Table, column: int):
        return self.get_column_header(column).get_value()

    def get_row_header(self: Table, row: int):
        header = Cell(self.component.get_row_header(row))
        return header

    def get_row_name(self: Table, column: int):
        return self.get_row_header(column).get_value()

    def is_selected(self: Table, row: int = None, column: int = None):
        if row is None:
            return self.component.is_column_selected(column)
        elif column is None:
            return self.component.is_row_selected(row)
        else:
            return self.component.is_selected(row, column)

    def get_row(self: Table, row: int):
        r = []
        for i in range(int(self.__get_columns_for_row())):
            r.append(self.get_cell(row, i))
        return Row(r)