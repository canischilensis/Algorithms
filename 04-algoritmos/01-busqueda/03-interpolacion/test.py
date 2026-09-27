import pytest
from interpolation_search_recursive import interpolation_search_recursive
from Interpolation_Search import interpolation_search

# ========================================
# TESTS 🔄 INTERPOLATION_SEARCH_RECURSIVE
# ========================================
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
def test_interpolation_search_recursive(lista, elemento, expected):
    result = interpolation_search_recursive(lista, elemento)
    if result == expected:
        print(f"✅ Algoritmo recursivo 🔄 ha pasado la prueba para {elemento} en {lista}")
    else:
        print(f"❌ Algoritmo recursivo 🔄 falló para {elemento} en {lista}: se esperaba {expected} pero retornó {result}")
    assert result == expected

# =========================================
# TESTS 🔁 INTERPOLATION_SEARCH (ITERATIVO)
# =========================================
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
def test_interpolation_search(monkeypatch, capsys, lista, elemento, expected):
    outputs = []

    def fake_print(msg):
        outputs.append(msg)

    monkeypatch.setattr("builtins.print", fake_print)
    interpolation_search(lista, elemento)

    found = [line for line in outputs if "el algoritmo lo ubico en" in line]
    
    if expected == -1:
        assert not found, f"❌ Se esperaba que no se encontrara {elemento} en {lista}, pero se encontró algo."
        print(f"✅ Algoritmo iterativo 🔁 pasó la prueba para {elemento} (no existe en la lista)")
    else:
        assert found, f"❌ No se encontró salida esperada en la impresión para {elemento} en {lista}"
        pos = int(found[0].split("posicion")[1].split(",")[0].strip())
        assert pos == expected, f"❌ Posición incorrecta: se esperaba {expected} pero se obtuvo {pos}"
        print(f"✅ Algoritmo iterativo 🔁 pasó la prueba para {elemento} en {lista}")