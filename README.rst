Edgy JSON
=========

Are mature, full-featured libraries too stable for you?

Do you like to remain at the forefront of bleeding edge technologies?

Do you burn yourself on coffee that isn’t cool yet?

This is `JSON Schema`_ for hipsters like you!

Documentation
-------------

Here is the `full documentation`_.

::

    edgy.check(schema, data)

I wanted to write a zero-function library, but that’s so edgy it’s
illegal.

Example

::

    edgy.check({"x": "int"}, {"x": 7})

Note that you're not passing JSON strings, you're giving the function
some standard python objects to work with.

Examples
--------

Just work things out from these.

Basics
~~~~~~

Schema

::

    {"x": "int", "y": "string"}

Example Data

::

    {"x": 10, "y": "hello"}

Or
~~

Lists in the schema will match any element.

Schema

::

    {"x": ["int", "string"]}

Example Data

::

    {"x": 3}

    {"x": "edgy"}

Schema

::

    [
        {"x": "int"},
        {"y": "string"}
    ]

Example Data

::

    {"x": -20}

    {"y": "not cool yet"}

Lists
~~~~~

Schema

::

    {
        "__type__": "list",
        "__item__": "int"
    }

Example Data

::

    [1, 2, 3, 4]

Extended Integers
~~~~~~~~~~~~~~~~~

Schema

::

    {
        "__type__": "int",
        "__minimum__": 10,
        "__maximum__": 20
    }

Example Data

::

    15

String Equality
~~~~~~~~~~~~~~~

Schema

::

    {
        "__type__": "string",
        "__equals__": "Hello"
    }

Example Data

Regular Expression Matching
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Uses Python's regex module, re.

::

    "Hello"

Schema

::

    {
        "__type__": "string",
        "__matches__": "[A-Z ]*"
    }

Example Data

::

    "UPPERCASE ONLY"

Recursion
~~~~~~~~~

Schema

::

    {
        "__named__":
        {
            "list_of_ints":
            {
                "__type__": "list",
                "__item__":
                [
                    "int",
                    "@list_of_ints"
                ]
            }
        },
        "__this__": "@list_of_ints"
    }

Example Data

::

    [6, 3, 7, [3, 6, 3], 6, [20]]

.. _JSON Schema: https://json-schema.org
.. _full documentation: http://dxsmiley.github.io/edgy-json/docs
