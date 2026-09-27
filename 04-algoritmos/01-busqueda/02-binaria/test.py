import pytest
from Binary_search_recursive import binary_search_recursive
from Binary_search import binary_search

# ===============================
# TESTS PARA BINARY_SEARCH_RECURSIVE
# ===============================
@pytest.mark.parametrize("lista, elemento, expected", [
    ([1, 3, 5, 7, 9], 5, 2),
    ([0, 10, 20, 30, 40], 30, 3),
    ([100, 200, 300], 100, 0),
    ([1, 2, 3, 4, 5, 6], 6, 5),
    ([10, 20, 30, 40, 50], 25, -1),
    ([1], 1, 0),
    ([1], 0, -1),
    ([1, 3, 5, 7], 1, 0),
    ([1, 3, 5, 7], 7, 3),
    ([5, 10, 15, 20], 17, -1),
    ([2, 4, 6, 8, 10, 12, 14], 8, 3),
    ([11, 13, 15, 17, 19], 13, 1),
    ([0, 1, 2, 3, 4, 5, 6], 4, 4),
    ([0, 1, 2, 3, 4, 5, 6], 7, -1),
    ([99, 100, 101], 100, 1),
])
def test_binary_search_recursive(lista, elemento, expected):
    result = binary_search_recursive(lista, elemento)
    if result == expected:
        print(f"✅ Recursive test passed for {elemento} in {lista}")
    else:
        print(f"❌ Recursive test failed for {elemento} in {lista}. Got {result}, expected {expected}")
    assert result == expected

# ===============================
# TESTS PARA BINARY_SEARCH (ITERATIVO)
# ===============================
@pytest.mark.parametrize("lista, elemento, expected", [
    ([1, 3, 5, 7, 9], 5, 2),
    ([0, 10, 20, 30, 40], 30, 3),
    ([100, 200, 300], 100, 0),
    ([1, 2, 3, 4, 5, 6], 6, 5),
    ([10, 20, 30, 40, 50], 25, -1),
    ([1], 1, 0),
    ([1], 0, -1),
    ([1, 3, 5, 7], 1, 0),
    ([1, 3, 5, 7], 7, 3),
    ([5, 10, 15, 20], 17, -1),
    ([2, 4, 6, 8, 10, 12, 14], 8, 3),
    ([11, 13, 15, 17, 19], 13, 1),
    ([0, 1, 2, 3, 4, 5, 6], 4, 4),
    ([0, 1, 2, 3, 4, 5, 6], 7, -1),
    ([99, 100, 101], 100, 1),
])
def test_binary_search(monkeypatch, capsys, lista, elemento, expected):
    outputs = []

    def fake_print(msg):
        outputs.append(msg)

    monkeypatch.setattr("builtins.print", fake_print)
    binary_search(lista, elemento)

    found = [line for line in outputs if "se encuentra en la posicion" in line]
    if expected == -1:
        assert not found
        print(f"✅ Iterative test passed (not found) for {elemento} in {lista}")
    else:
        assert found
        pos = int(found[0].split("posicion")[1].split(",")[0].strip())
        if pos == expected:
            print(f"✅ Iterative test passed for {elemento} in {lista}")
        else:
            print(f"❌ Iterative test failed for {elemento} in {lista}. Got {pos}, expected {expected}")
        assert pos == expected
