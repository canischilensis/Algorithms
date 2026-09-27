import pytest
from Linear_search_recursive import linear_search_recursive
from Search_linear import linear_search

# Tests para linear_search_recursive
@pytest.mark.parametrize("lista, elemento, expected", [
    ([1, 3, 5], 5, 2),
    ([0, -1, -2], -2, 2),
    ([100], 100, 0),
    ([4, 5, 6, 7, 8], 7, 3),
    ([1, 1, 1, 1], 1, 0),
    ([2, 4, 6], 1, -1),
    ([], 9, -1),
    ([9, 8, 7, 6], 6, 3),
    ([0, 2, 4, 6, 8], 0, 0),
    ([5, 10, 15, 20, 25], 25, 4),
    ([3, 6, 9], 6, 1),
    ([10, 20, 30, 40], 30, 2),
    ([1, 3, 5, 7, 9], 2, -1),
    ([0, 0, 0], 0, 0),
    ([1, 2, 3, 4, 5], 6, -1),
])
def test_linear_search_recursive(lista, elemento, expected):
    result = linear_search_recursive(lista, 0, elemento)
    if result == expected:
        print(f"✅ Recursive test passed for {elemento} in {lista}")
    else:
        print(f"❌ Recursive test failed for {elemento} in {lista}. Got {result}, expected {expected}")
    assert result == expected

# Tests para linear_search
@pytest.mark.parametrize("lista, elemento, expected", [
    ([1, 3, 5], 5, 2),
    ([0, -1, -2], -2, 2),
    ([100], 100, 0),
    ([4, 5, 6, 7, 8], 7, 3),
    ([1, 1, 1, 1], 1, 0),
    ([2, 4, 6], 1, -1),
    ([], 9, -1),
    ([9, 8, 7, 6], 6, 3),
    ([0, 2, 4, 6, 8], 0, 0),
    ([5, 10, 15, 20, 25], 25, 4),
    ([3, 6, 9], 6, 1),
    ([10, 20, 30, 40], 30, 2),
    ([1, 3, 5, 7, 9], 2, -1),
    ([0, 0, 0], 0, 0),
    ([1, 2, 3, 4, 5], 6, -1),
])
def test_linear_search(monkeypatch, capsys, lista, elemento, expected):
    outputs = []

    def fake_print(msg):
        outputs.append(msg)

    monkeypatch.setattr("builtins.print", fake_print)
    linear_search(lista, elemento)

    found = [line for line in outputs if "se ha encontrado" in line]
    if expected == -1:
        assert not found
        print(f"✅ Linear test passed (not found) for {elemento} in {lista}")
    else:
        assert found
        position_reported = int(found[0].split("posicion")[1].split(",")[0].strip())
        if position_reported == expected:
            print(f"✅ Linear test passed for {elemento} in {lista}")
        else:
            print(f"❌ Linear test failed: Expected position {expected}, got {position_reported}")
        assert position_reported == expected