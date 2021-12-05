from __future__ import annotations
from components import button
from typing import *

import gi
gi.require_version('Atspi', '2.0')
from gi.repository import Atspi

class Utils:
    def tree_walk(self: Utils, obj):
        yield obj
        for i in range(obj.get_child_count()):
            yield from self.tree_walk(obj.get_child_at_index(i))

    def set_ipm_object(self: Utils, obj: Atspi.Object):
        if obj.get_role_name() == "push button":
            return button.Button(obj)
        elif obj.get_role_name() == "combo box":
            return componentType.ComboBox(obj)
        elif obj.get_role_name() == "label":
            return componentType.Label(obj)
        elif obj.get_role_name() == "table":
            return componentType.Table(obj)
        elif obj.get_role_name() == "text":
            return componentType.Entry(obj)
        elif obj.get_role_name() == "spin button":
            return componentType.SpinButton(obj)
        elif obj.get_role_name() == "frame" or obj.get_role_name() == "panel":
            return componentType.Container(obj)


    def atspi_to_ipm_object(self: Utils, list: List[Atspi.Object]) -> List[E2eComponent]:
        childrens = []
        for obj in list:
            childrens.append(set_ipm_object(obj))
        return childrens
