from coverage_bug import covered_function


def test_three():
    covered_function(3)


def test_twenty():
    covered_function(20)


def test_billion():
    covered_function(1000 * 1000 * 1000)
