from zahlen.stat import ss, corelation, determinate

x = (5, 6, 4, 5, 1)
y = (7, 6, 4, 9, 3)

def test_ss_success():
    result = ss(x, y)

    assert result.ok

def test_ss_not_eq():
    result = ss(x[:3], y)

    assert result.err

def test_ss_one_element():
    result = ss([1], [23])

    assert result.err

def test_corelation():
    result = corelation(x, y)

    assert result.ok

def test_determinate():
    result = determinate(x, y)

    assert result.ok