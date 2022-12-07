# Data Model

Python supports special methods (magic methods) that implement a variety of protocols.

* Python tries to make your code look just a pythonic as the rest
* protocols allow objects to be used in more places or in a more pythonic API

Examples: [DataModelExamples](notebooks/DataModelExamples.ipynb)

## Overview


The set of methods is quite large (50+) but falls into a few categories.

## Initialization and Construction

* `__new__`
* `__init__`
* `__del__`

## Comparisons

* `__eq__`
* `__ne__`
* `__lt__`
* `__gt__`
* `__le__`
* `__ge__`

## Unary operators and functions

* `__pos__`
* `__neg__`
* `__abs__`
* `__invert__`
* `__round__`
* `__floor__`
* `__ceil__`
* `__trunc__`

## Augmented assignment

* `__iadd__`
* `__isub__`
* `__imul__`
* `__ifloordiv__`
* `__idiv__`
* `__itruediv__`
* `__imod__`
* `__ipow__`
* `__ilshift__`
* `__irshift__`
* `__iand__`
* `__ior__`
* `__ixor__`

## Type Conversions

* `__int__`
* `__float__`
* `__complex__`
* `__oct__`
* `__hex__`
* `__index__`
* `__trunc__`

## String Magic

* `__str__`
* `__repr__`
* `__unicode__`
* `__format__`
* `__hash__`
* `__nonzero__`
* `__dir__`
* `__sizeof__`

## Attribute Magic

* `__getattr__`
* `__setattr__`
* `__delattr__`

## Operator Magic

* `__add__`
* `__sub__`
* `__mul__`
* `__floordiv__`
* `__truediv__`
* `__mod__`
* `__pow__`


Additionally, there are various protocols that are using special methods as well.

* [https://docs.python.org/3/reference/datamodel.html#special-method-names](https://docs.python.org/3/reference/datamodel.html#special-method-names)

Another partitioning of the special methods:

* custom attribute access (descriptors)
* class creation
* instance and subclass checks
* emulating generic types
* callable objects
* container types
* numeric types
* context managers
* custom positional arguments for class pattern matching
* async iteration

