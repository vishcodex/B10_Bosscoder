# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

from functools import total_ordering
from typing import List

from numpy import mat


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0]*n for i in range(n)]
        value = 1
        irow = 0
        row = n-1
        icol = 0
        col = n-1
        
        while irow <= row and icol <= col:
            for i in range(icol, col+1):
                mat[irow][i] = value
                value += 1
            for i in range(irow+1, row+1):
                mat[i][col] = value
                value += 1
            if irow < row and icol < col:
                for i in range(col-1, icol-1, -1):
                    mat[row][i] = value
                    value += 1
                for i in range(row-1, irow, -1):
                    mat[i][icol] = value
                    value += 1
            irow += 1
            row -= 1
            icol += 1
            col -= 1
        return mat

if __name__ == '__main__':
    ob = Solution()
    res = ob.generateMatrix(n = 3)
    print(res)