from types import DynamicClassAttribute

Enum = None

class property(DynamicClassAttribute):

    def __get__(self, instance, owncls=None):
        if instance is None:
            return owncls._member_map_[self.name]
        else:
            return self.fget(instance)

    def __set_name__(self, owncls, name):
        self.name = name


class _member:

    def __init__(self, value):
        self.value = value

    def __set_name__(self, enum_class, member_name):

        value = self.value
        enum_member = enum_class._new_member_(enum_class)
        if not hasattr(enum_member, '_value_'):
            enum_member._value_ = value[0]
            enum_member._name_ = value[1]
            enum_member._member_type_ = 'PY2END_' + enum_class.__class_name__.upper() + '_' + member_name

        value = enum_member._value_
        enum_member._type_ = member_name
        enum_class._member_names_.append(member_name)
       
        redirect = property()
        redirect.__set_name__(enum_class, member_name)

        setattr(enum_class, member_name, redirect)

        enum_class._member_map_[member_name] = enum_member
        enum_class._value2member_map_.setdefault(value, enum_member)


class _Dict(dict):

    def __init__(self):

        super().__init__()
        self._member_names = {}

    def __setitem__(self, key, value):

        if ( len(key) > 4 and key[:2] == key[-2:] == '__' ):
            key = '_order_' if key == '__order__' else key
        elif not hasattr(value, '__get__'):
            self._member_names[key] = None
        
        super().__setitem__(key, value)


class _Type(type):

    @classmethod
    def __prepare__(metacls, cls, bases, **kwds):
        return _Dict()

    def __new__(metacls, cls, bases, classdict, **kwds):

        member_names = classdict._member_names
        
        classdict = dict(classdict.items())
        classdict['_new_member_'] = classdict.get('__new__', None) or object.__new__
        classdict['_member_names_'] = []
        classdict['_member_map_'] = {}
        classdict['_value2member_map_'] = {}
        classdict['__doc__'] = "Enumeration of %s." % (cls, )
        classdict['__class_name__'] = cls
        classdict['__class__'] = "<enum 'py2Enum.%s'>" % cls
        classdict['__created__'] = 0
        for name in member_names:
            classdict[name] = _member(classdict[name])

        enum_class = super().__new__(metacls, cls, bases, classdict, **kwds)
        enum_class.__created__ = 1

        return enum_class

    def __class__(self):
        return self.__class__

    def __dir__(cls):
        enum_attrs = set(cls.__dict__)
        enum_attrs.remove('__module__')
        enum_attrs.remove('_new_member_')
        enum_attrs.remove('__created__')
        enum_attrs.remove('__class_name__')
        enum_attrs.add('values')
        enum_attrs.add('get_name')
        return sorted(enum_attrs)

    def __iter__(cls):
        return (cls._member_map_[name] for name in cls._member_names_)

    def __len__(cls):
        return len(cls._member_names_)

    def __repr__(cls):
        return "<Enum type py2End.%s>" % (cls.__name__, )

    def __setattr__(cls, name, value):

        if cls.__dict__.get('__created__',) == 1:
            raise AttributeError("cannot set %r in enum %s" % (name,cls.__dict__.get('_class_')))
        if name in cls.__dict__.get('_member_map_', {}):
            raise AttributeError('Cannot reassign member %r.' % (name, ))            
        super().__setattr__(name, value)

    def get_name(self, type):
        return type._name_

    @property
    def values(self):
        return {k:v._type_ for k,v in self._value2member_map_.items()}

    
class E2Enum(metaclass=_Type):

    def __new__(cls, value):
        return cls._value2member_map_[value]

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "<Enum %s of type py2End.%s>" % (self._type_, self.__class_name__)
        
    def __hash__(self):
        return self._value_

    def __dir__(self):
        return ['__class__', '__doc__', 'name', 'value', 'type']

    @property
    def name(self):
        return self._name_

    @property
    def value(self):
        return self._value_

    @property
    def type(self):
        return self._type_

    @property
    def member_type(self):
        return self._member_type_