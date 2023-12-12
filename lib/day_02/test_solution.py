from .solution import parse, solve


data = """
some
example input
"""

def test_solution():
    assert solve(parse(data)) == 42
