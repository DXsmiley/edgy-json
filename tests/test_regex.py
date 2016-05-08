import edgy


def test_simple():
    assert edgy.check({'__type__': 'string', 'matches': '.*'}, 'hello')
    assert edgy.check({'__type__': 'string', 'matches': 'o*'}, 'ooo')


def test_spaced_number():
    assert edgy.check({'__type__': 'string', 'matches': '[0-9 ]+'}, '01 2345 6789')


def test_failure():
    assert edgy.check({'__type__': 'string', 'matches': '.*'}, 'hello')
    assert not edgy.check({'__type__': 'string', 'matches': 'o*'}, 'ood')
