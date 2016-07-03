import edgy


SCHEMA = \
{
    '__named__':
    {
        'schema':
        [
            'string',
            True,
            False,
            {
                '__type__': 'list',
                '__item__': '@schema'
            },
            {
                '~__named__': ['none', '@named'],
                '~__this__': ['none', '@schema'],
                '__extra__': 'anything',
                '__this__':
                [
                    {
                        '~__named__': 'anything',
                        '~__this__': 'anything',
                        '~__type__': ['none', 'object'],
                        '__extra__': '@schema'
                    },
                    {
                        '~__named__': 'anything',
                        '~__this__': 'anything',
                        '~__type__':
                        {
                            '__type__': 'string',
                            '__equals__': 'int'
                        },
                        '__equals__': ['none', 'int'],
                        '__minimum__': ['none', 'int'],
                        '__maximum__': ['none', 'int']
                    },
                    {
                        '~__named__': 'anything',
                        '~__this__': 'anything',
                        '~__type__':
                        {
                            '__type__': 'string',
                            '__equals__': 'string'
                        },
                        '__equals__': ['none', 'string'],
                        '__matches__': ['none', 'string']
                    },
                    {
                        '~__named__': 'anything',
                        '~__this__': 'anything',
                        '~__type__':
                        {
                            '__type__': 'string',
                            '__equals__': 'list'
                        },
                        '~__item__': '@schema'
                    }
                ]
            }
        ],
        'named':
        {
            '__extra__': '@schema'
        }
    },
    '__this__': '@schema'
}


def test_schema():
    assert edgy.check(SCHEMA, SCHEMA)
