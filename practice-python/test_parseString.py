from parcingSortingNumbers import parseString

def test_parseString():
    assert parseString(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]) == ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]