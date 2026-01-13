class Solution:
    def row_major_traverse(self, matrix: list[list[int]]) -> list[int]:
        if not matrix:
            return []

        row: int = len(matrix)
        col: int = len(matrix[0])

        list = []
        for i in range(row):
            for j in range(col):
                list.append(matrix[i][j])

        return list
