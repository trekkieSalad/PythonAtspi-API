from .e2Enum import E2Enum
import gi
gi.require_version('Atspi', '2.0')
from gi.repository import Atspi

class E2CollectionMatchType(E2Enum):
    INVALID = (hash(Atspi.CollectionMatchType(0)), 'invalid')
    ALL = (hash(Atspi.CollectionMatchType(1)), 'all')
    ANY = (hash(Atspi.CollectionMatchType(2)), 'any')
    NONE = (hash(Atspi.CollectionMatchType(3)), 'none')
    EMPTY = (hash(Atspi.CollectionMatchType(4)), 'empty')
    LAST_DEFINED = (hash(Atspi.CollectionMatchType(5)), 'last_defined')

class E2CollectionSortOrder(E2Enum):
    INVALID = (hash(Atspi.CollectionSortOrder(0)), 'invalid')
    CANONICAL = (hash(Atspi.CollectionSortOrder(1)), 'canonical')
    FLOW = (hash(Atspi.CollectionSortOrder(2)), 'flow')
    TAB = (hash(Atspi.CollectionSortOrder(3)), 'tab')
    REVERSE_CANONICAL = (hash(Atspi.CollectionSortOrder(4)), 'reverse_canonical')
    REVERSE_FLOW = (hash(Atspi.CollectionSortOrder(5)), 'reverse_flow')
    REVERSE_TAB = (hash(Atspi.CollectionSortOrder(6)), 'reverse_tab')
    LAST_DEFINED = (hash(Atspi.CollectionSortOrder(7)), 'last_defined')

class E2CollectionTreeTraversalType(E2Enum):
    RESTRICT_CHILDREN = (hash(Atspi.CollectionTreeTraversalType(0)), 'restrict_children')
    RESTRICT_SIBLINGS = (hash(Atspi.CollectionTreeTraversalType(1)), 'restrict_siblings')
    INORDER = (hash(Atspi.CollectionTreeTraversalType(2)), 'inorder')
    LAST_DEFINED = (hash(Atspi.CollectionTreeTraversalType(3)), 'last_defined')