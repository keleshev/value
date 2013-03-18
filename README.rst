Implementation of Value Object Pattern for Python
=================================================

`From Wikipedia <http://en.wikipedia.org/wiki/Value_object>`_:

  A **value object** is a small object that represents a
  simple entity whose equality isn't based on identity: i.e.
  two value objects are equal when they have the same value,
  not necessarily being the same object.

By default (if you subclass from ``object``) Python follows
"reference semantics", i.e. two objects are equal if they
are the same instance.  ``Value`` class implements "value
semantics", i.e. if you subclass it your objects will be
equall if they hold the same data.

This implementation will also inspect your ``__init__``
signature to automatically assign instance variables and
produce a nice ``__repr__`` for your objects, dogether with
a suitable ``__hash__`` implementation.

Instead of asigning each instance variable manually:

.. code:: python

    >>> class Date(object):
    ...
    ...     def __init__(self, year, month=1, day=1):
    ...         self.year = year
    ...         self.month = month
    ...         self.day = day

``Value`` defines ``__new__`` that will look at your
``__init__`` signature and assign instance variables based
on it:

.. code:: python

    >>> from value import Value
    ...
    >>> class Date(Value):
    ...
    ...     def __init__(self, year, month=1, day=1):
    ...         pass
    ...
    >>> Date(2013, 3).year == 2013
    True
    >>> Date(2013, 3).month == 3
    True
    >>> Date(2013, 3).day == 1
    True

``Value`` defines ``__eq__`` and ``__ne__`` to implement
value object semantics, i.e. objects holding the same data
are compared equal:

.. code:: python

    >>> Date(2013, 3, 18) == Date(2013, 3, 18)
    True
    >>> Date(2013, 3, 18) != Date(1988)
    True

``Value`` also defines ``__repr__`` for you based on
``__init__`` signature:

.. code:: python

    >>> repr(Date(2013, 3, 18))
    'Date(2013, 3, 18)'
    >>> repr(Date(1988, 1, 1))
    'Date(1988)'

``Value`` also defines ``__hash__`` for you, so that
instances could be used in sets and as dictionary keys.

Installation
------------------------------------------------------------

Use `pip <http://pip-installer.org>`_ or easy_install::

    pip install value==0.1.0

Alternatively, you can just drop ``value.py`` file into your
project—it is self-contained.

- **value** is tested with Python 2.6, 2.7, 3.2, 3.3 and PyPy.
- **value** follows `semantic versioning <http://semver.org>`_.
