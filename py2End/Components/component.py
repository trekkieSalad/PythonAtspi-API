from __future__ import annotations
from typing import Dict, Any, List, Tuple
from .container import Container
from utils import *

import gi
gi.require_version('Atspi', '2.0')
from gi.repository import Atspi


class E2eComponent:

    # Constructor

    def __init__(self: E2eComponent, obj: Atspi.Object) -> None:
        self.__index = obj.get_index_in_parent()
        self.__type = obj.get_role_name()
        self.__component = obj
        self.__attributes = obj.get_attributes()

    # Getters for attributes

    def get_value(self: E2eComponent) -> str:
        return self.__value

    def get_type(self: E2eComponent) -> str:
        return self.__type

    def get_index(self: E2eComponent) -> int:
        return self.__index

    def get_attributes(self: E2eComponent) -> Dict[str, Any]:
        return self.__attributes

    def get_component(self: E2eComponent) -> Atspi.Object:
        return self.__component

    # Public methods

    def get_parent(self: E2eComponent) -> E2eComponent:
        return Utils.to_e2e_object(self.__parent())

    def get_size(self: E2eComponent) -> Tuple[int, int]:
        point = self.__component.get_component_iface().get_size()
        return point.x, point.y

    def get_position(self: E2eComponent, n: int) -> Tuple[int, int]:
        point = self.__component.get_component_iface().get_extents(Atspi.CoordType(n))
        return point.x, point.y

    def get_ancestors(self: E2eComponent) -> List[E2eComponent]:
        ancestors = self.__ancestors()
        return Utils.to_e2e_list(ancestors)

    def is_child_of(self: E2eComponent, parent: Container) -> bool:
        return self.__component.get_parent() == parent.get_component()

    def is_descendant_of(self: E2eComponent, ancestor: Container) -> bool:
        return ancestor.get_component() in self.get_ancestors()

    # Private methods

    def __ancestors(self: E2eComponent) -> List[Atspi.Object]:
        ancestors = []
        last_ancestor = self.__component.get_parent()
        while last_ancestor is not None:
            ancestors.append(last_ancestor)
            last_ancestor = last_ancestor.get_parent()
        return ancestors

    def __parent(self: E2eComponent) -> Atspi.Object:
        return self.__component.get_parent()
