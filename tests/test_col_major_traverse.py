from src.col_major_travers import Solution


def test_col_travers():
    matrix = [[1, 2], [4, 3], [5, 6]]

    sol = Solution()
    assert sol.solution(matrix) == [1, 4, 5, 2, 3, 6]
