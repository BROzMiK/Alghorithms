from src.flip_characters import Solution


def test_flip_char():
    arr = ["a", "b", "r", "g"]
    sol = Solution()

    assert sol.solution(arr) == ["g", "r", "b", "a"]
