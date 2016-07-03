import edgy


def test_simple():
    assert edgy.check({'__type__': 'string', '__matches__': '.*'}, 'hello')
    assert edgy.check({'__type__': 'string', '__matches__': 'o*'}, 'ooo')


def test_spaced_number():
    assert edgy.check({'__type__': 'string', '__matches__': '[0-9 ]+'}, '01 2345 6789')


def test_failure():
    assert edgy.check({'__type__': 'string', '__matches__': '.*'}, 'hello')
    assert not edgy.check({'__type__': 'string', '__matches__': 'o*'}, 'ood')
