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
                            'equals': 'int'
                        },
                        'equals': ['none', 'int'],
                        'minimum': ['none', 'int'],
                        'maximum': ['none', 'int']
                    },
                    {
                        '~__named__': 'anything',
                        '~__this__': 'anything',
                        '~__type__':
                        {
                            '__type__': 'string',
                            'equals': 'string'
                        },
                        'equals': ['none', 'string'],
                        'matches': ['none', 'string']
                    },
                    {
                        '~__named__': 'anything',
                        '~__this__': 'anything',
                        '~__type__':
                        {
                            '__type__': 'string',
                            'equals': 'list'
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
