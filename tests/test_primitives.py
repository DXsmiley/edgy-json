import edgy


generic_items = [
    False,
    True,
    7,
    3.1415,
    'Hello, World!',
    [],
    {},
    ['yes!'],
    {'x': 2},
    None
]


def test_nothing():
    for i in generic_items:
        assert edgy.check('nothing', i) == False


def test_anything():
    for i in generic_items:
        assert edgy.check('anything', i) == True


def test_string():
    for i in generic_items:
        assert edgy.check('string', i) == isinstance(i, str)


def test_integer():
    for i in generic_items:
        assert edgy.check('int', i) == isinstance(i, int)


def test_float():
    for i in generic_items:
        assert edgy.check('float', i) == isinstance(i, float)


def test_bool():
    for i in generic_items:
        assert edgy.check('bool', i) == isinstance(i, bool)


def test_true():
    for i in generic_items:
        assert edgy.check(True, i) == (i is True)


def test_false():
    for i in generic_items:
        assert edgy.check(False, i) == (i is False)


def test_none():
    for i in generic_items:
        assert edgy.check('none', i) == (i is None)

