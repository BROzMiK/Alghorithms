class Solution:
    def solution(self, matrix: list[list[int]]) -> list[int]:
        if not matrix:
            return []

        rows: int = len(matrix)
        cols: int = len(matrix[0])

        list = []
        for col in range(cols):
            for row in range(rows):
                list.append(matrix[row][col])

        return list
