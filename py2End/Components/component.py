from __future__ import annotations
from typing import Dict, Any, List, Tuple
from utils import Utils

import gi
gi.require_version('Atspi', '2.0')
from gi.repository import Atspi


class E2eComponent:

    def __init__(self: E2eComponent, obj: Atspi.Object) -> None:
        self.__index = obj.get_index_in_parent()
        self.__type = obj.get_role_name()
        self.__component = obj
        self.__attributes = obj.get_attributes()

    # getters de atributos

    def get_value(self: E2eComponent) -> str:
        return self.__value

    def get_type(self: E2eComponent) -> str:
        return self.__type

    def get_index(self: E2eComponent) -> int:
        return self.__index

    def get_attributes(self: E2eComponent) -> Dict[str, Any]:
        return self.__attributes

    # metodos publicos

    def get_parent(self: E2eComponent) -> str:
        return self.__component.get_parent()

    def get_childrens(self: E2eComponent) -> List[E2eComponent]:
        childrens = [self.component.get_child_at_index(i)
                     for i in range(self.component.get_child_count())]
        return Utils.atspi_to_ipm_object(childrens)

    def get_childrens_number(self: E2eComponent) -> int:
        return len(self.get_childrens())

    def get_descendants(self: E2eComponent) -> List[E2eComponent]:
        childrens = []
        for obj in Utils.tree_walk(self.component):
            childrens.append(obj)
        return Utils.atspi_to_ipm_object(childrens)

    def get_descendants_number(self: E2eComponent) -> int:
        return len(self.get_descendants())

    def get_size(self: E2eComponent) -> Tuple[int, int]:
        point = self.component.get_component_iface().get_size()
        return point.x, point.y

    def get_position(self: E2eComponent, n: int) -> Tuple[int, int]:
        point = self.component.get_component_iface().get_extents(Atspi.CoordType(n))
        return point.x, point.y
