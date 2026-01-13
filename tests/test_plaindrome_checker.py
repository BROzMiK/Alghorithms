from src.palindrome_checker import Solution
import pytest


@pytest.mark.parametrize(
    "s, expected",
    [
        ("man a nam", True),
        ("?,Was it a car or a cat I saw Otis", False),
        ("A man, a plan, a canal: Panama", True),
    ],
)
def test_palindrome_checker(s, expected):
    sol = Solution()

    assert sol.palindrome_checker(s) is expected
