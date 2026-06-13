from scoring import reducing_score

def test_normal_reduction():
    assert reducing_score(50) == 40

def test_floors_at_zero():
    assert reducing_score(5) == 0

def test_already_zero():
    assert reducing_score(0) == 0