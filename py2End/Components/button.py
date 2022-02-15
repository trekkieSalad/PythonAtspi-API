from __future__ import annotations
from component import E2eComponent


import gi
gi.require_version('Atspi', '2.0')
from gi.repository import Atspi


class Button(E2eComponent):

    def __init__(self: Button, obj: Atspi.Object):
        super().__init__(obj)
        self.name = obj.get_name() or 'Button_'

    def do(self, action):
        for i in range(self.component.get_n_actions()):
            iname = self.component.get_action_name(i)
            if iname == action or str(i) == action:
                self.component.do_action(i)
                return True
        return False