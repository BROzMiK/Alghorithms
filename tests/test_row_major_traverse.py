from src.row_major_travers import Solution


def test_traverse_happy():
    sol = Solution()
    list = [[1, 3, 4], [5, 1, 3]]
    assert sol.row_major_traverse(list) == [1, 3, 4, 5, 1, 3]
