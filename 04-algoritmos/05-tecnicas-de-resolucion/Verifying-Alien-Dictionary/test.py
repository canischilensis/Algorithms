import pytest

from alien_dictionary import alien_sorted  # Asumiendo que la función está en alien_dictionary.py

@pytest.mark.parametrize("words, order, expected", [
    # Caso básico ordenado
    (["hola", "holaa", "holb"], "hlabcdefgijkmnopqrstuvwxyz", True),
    # Lista vacía o un solo elemento siempre ordenada
    ([], "hlabcdefgijkmnopqrstuvwxyz", True),
    (["solo"], "hlabcdefgijkmnopqrstuvwxyz", True),
    # Prefijo: "app" precede "apple"
    (["app", "apple"], "hlabcdefgijkmnopqrstuvwxyz", True),
    # No ordenado: diferencia en la primera letra
    (["bello", "apple"], "hlabcdefgijkmnopqrstuvwxyz", False),
    # No ordenado: misma prefijo, segunda palabra más corta
    (["apple", "app"], "hlabcdefgijkmnopqrstuvwxyz", False),
    # Orden personalizado: 'a' > 'b'
    (["a", "b"], "bacdefghijklmnopqrstuvwxyz", False),
    # Repetición de palabras
    (["test", "test", "test"], "hlabcdefgijkmnopqrstuvwxyz", True),
    # Orden con caracteres al final
    (["xyz", "z"], "hlabcdefgijkmnopqrstuvwxyz", True),
])
def test_alien_sorted(words, order, expected):
    result = alien_sorted(words, order)
    if result == expected:
        print(f"✅ Test passed: words={words}, order={order}")
    else:
        print(f"❌ Test failed: words={words}, order={order}")
    assert result == expected

def test_invalid_characters():
    with pytest.raises(KeyError):
        alien_sorted(["hola", "mundo"], "abc")
        print("✅ Test passed: invalid characters raised KeyError")

if __name__ == "__main__":
    pytest.main()