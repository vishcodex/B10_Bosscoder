from typing import List



def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    lo, hi = 0, len(matrix) * len(matrix[0]) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        r = mid // len(matrix[0])
        c = mid % len(matrix[0])
        if matrix[r][c] == target: return True
        if target > matrix[r][c]: lo = mid + 1
        else: hi = mid - 1
    return False


print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))


# https://leetcode.com/problems/search-a-2d-matrix/discuss/1863617/Python-or-5-different-Solutions ( More approaches )


