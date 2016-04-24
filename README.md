# Edgy JSON

Are mature, full-featured libraries too stable for you?

Do you like to remain at the forefront of bleeding edge technologies?

Do you burn yourself on coffee that isn't cool yet?

This is [JSON Schema](https://json-schema.org) for hipsters like you!

## Documentation

    edgy.check(schema, data)

I wanted to write a zero-function library, but that's so edgy it's illegal.

## Examples

Just work things out from these.

### Basics

Schema

    {"x": "int", "y": "string"}

Example Data

    {"x": 10, "y": "hello"}

### Or

Lists in the schema will match any element.

Schema

    {"x": ["int", "string"]}

Example Data

    {"x", 3}

    {"x", "edgy"}

Schema

    [
        {"x": "int"},
        {"y": "string"}
    ]

Example Data

    {"x", -20}

    {"y": "not cool yet"}

### Lists

Schema

    {
        "__type__": "list",
        "__item__": "int"
    }

Example Data

    [1, 2, 3, 4]

### Extended Integers

Schema

    {
        "__type__": "int",
        "minimum": 10,
        "maximum": 20
    }

Example Data

    15

### Recursion

Schema

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

    [6, 3, 7, [3, 6, 3], 6, [20]]
