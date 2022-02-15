from __future__ import annotations
from component import *
from typing import Dict, Any, List, Tuple
from utils import *

import gi
gi.require_version('Atspi', '2.0')
from gi.repository import Atspi

class Container(E2eComponent):

    # Atributes

    # Constructor

    def __init__(self: Container, obj: Atspi.Object):
        super().__init__(obj)

    # Public Methods

    def get_childrens(self: Container) -> List[E2eComponent]:
        childrens = [self.component.get_child_at_index(i)
                     for i in range(self.component.get_child_count())]
        return Utils.to_e2e_list(childrens)

    def get_childrens_number(self: Container) -> int:
        return len(self.get_childrens())

    def get_descendants(self: Container) -> List[E2eComponent]:
        childrens = []
        for obj in Utils.tree_walk(self.component):
            childrens.append(obj)
        return Utils.to_e2e_list(childrens)

    def get_descendants_number(self: Container) -> int:
        return len(self.get_descendants())

    def is_parent_of(self: Container, child: E2eComponent) -> bool:
        return child.component.get_parent() == self.component
