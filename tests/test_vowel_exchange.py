from src.vowel_exchange import Solution
import pytest


@pytest.mark.parametrize(
    "s, expected",
    [
        ("random", "rondam"),
        ("afegijoku", "ufogijeka"),
        ("bcdf", "bcdf"),
        ("hello", "holle"),
    ],
)
def test_vowel_exchange(s, expected):
    sol = Solution()

    assert sol.vowel_exchange(s) == expected
