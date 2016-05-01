import edgy

def test_escape():
    assert edgy.check({'~__this__': 'int'}, {'__this__': 5})
