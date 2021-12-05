from .e2Enum import E2Enum
import gi
gi.require_version('Atspi', '2.0')
from gi.repository import Atspi

class E2EventType(E2Enum):
    KEY_PRESSED_EVENT = (hash(Atspi.EventType(0)), 'key pressed event')
    KEY_RELEASED_EVENT = (hash(Atspi.EventType(1)), 'key released event')
    BUTTON_PRESSED_EVENT = (hash(Atspi.EventType(2)), 'button pressed event')
    BUTTON_RELEASED_EVENT = (hash(Atspi.EventType(3)), 'button released event')

class E2KeyEventType(E2Enum):
    PRESSED = (hash(Atspi.KeyEventType(0)), 'pressed')
    RELEASED = (hash(Atspi.KeyEventType(1)), 'released')

class E2KeySynthType(E2Enum):
    PRESS = (hash(Atspi.KeySynthType(0)), 'press')
    RELEASE = (hash(Atspi.KeySynthType(1)), 'release')
    PRESSRELEASE = (hash(Atspi.KeySynthType(2)), 'press and release')
    SYM = (hash(Atspi.KeySynthType(3)), 'symbol')
    STRING = (hash(Atspi.KeySynthType(4)), 'string')
    LOCKMODIFIERS = (hash(Atspi.KeySynthType(5)), 'lock modifiers')
    UNLOCKMODIFIERS = (hash(Atspi.KeySynthType(6)), 'unlock modifiers')