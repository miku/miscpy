# Descriptors and Slots

* Descriptors implement the descriptor protocol

> In general, a descriptor is an object attribute with “binding behavior”, one
> whose attribute access has been overridden by methods in the descriptor
> protocol: __get__(), __set__(), and __delete__(). If any of those methods are
> defined for an object, it is said to be a descriptor.

What happens to `a.x` will depend:

* direct call: `x.__get__(a)`
* instance binding: `type(a).__dict__[x].__get__(a, type(a))`
* class binding: `A.__dict__['x'].__get__(None, A)`

Descriptors are a level of indirection, allowing to customize attribute access.

> To use the descriptor, it must be stored as a **class variable** in another class.

See:

* [notebooks/Descriptors.ipynb](notebooks/Descriptors.ipynb)

