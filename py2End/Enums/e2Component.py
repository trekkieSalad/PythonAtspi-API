from .e2Enum import E2Enum
import gi
gi.require_version('Atspi', '2.0')
from gi.repository import Atspi

class E2ComponentLayer(E2Enum):
    INVALID = (hash(Atspi.ComponentLayer(0)), 'invalid')
    BACKGROUND = (hash(Atspi.ComponentLayer(1)), 'background')
    CANVAS = (hash(Atspi.ComponentLayer(2)), 'canvas')
    WIDGET = (hash(Atspi.ComponentLayer(3)), 'widget')
    MDI = (hash(Atspi.ComponentLayer(4)), 'mdi')
    POPUP = (hash(Atspi.ComponentLayer(5)), 'popup')
    OVERLAY = (hash(Atspi.ComponentLayer(6)), 'overlay')
    WINDOW = (hash(Atspi.ComponentLayer(7)), 'window')
    LAST_DEFINED = (hash(Atspi.ComponentLayer(8)), 'last_defined')
    
class E2CoordType(E2Enum):
    SCREEN = (hash(Atspi.CoordType(0)), 'screen')
    WINDOW = (hash(Atspi.CoordType(1)), 'window')
    PARENT = (hash(Atspi.CoordType(2)), 'parent')