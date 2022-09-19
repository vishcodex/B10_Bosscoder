# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

from typing import List


class Solution:

    #  TWO POINTER APPROACH
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        left_max, right_max = height[i], height[j]
        res = 0
        while i < j:
            left_max = max(left_max, height[i])
            right_max = max(right_max, height[j])
            if left_max < right_max:
               res += left_max - height[i]
               i += 1
            else:
               res += right_max - height[j]
               j -= 1
        return res

    # # Solving using Dynamic Programming

    # def trap(self, height: List[int]) -> int:
    #         N = len(height)
    #         left_max = N * [0]
    #         right_max = N * [0]
    #         ans = 0
    #         for i in range(N):
    #             print("i", i)
    #             if i == 0:
    #                 left_max[i] = height[i]
    #                 right_max[N-1-i] = height[N-1-i]
    #             else:
    #                 left_max[i] = max(left_max[i-1], height[i])
    #                 right_max[N-1-i] = max(right_max[N-i], height[N-1-i])
                
    #         for i in range(N):
    #             ans += (min(left_max[i], right_max[i]) - height[i]) 
    #         return ans


    # BRUTEFORCE APPROACH

    # def trap(self, height: List[int]) -> int:
    #     n = len(height)
    #     left_val = height[0]
    #     left = [0]*n
    #     for i in range(0,n) :
    #         if left_val < height[i]:
    #             left_val = height[i]
    #             left[i] = left_val
    #         else:
    #             left[i] = left_val
    #     print("left :", left)

    #     right_val = height[-1]
    #     right = [0]*n
    #     for i in range(n-1, -1, -1):
    #         if right_val < height[i]:
    #             right_val = height[i]
    #             right[i] = right_val
    #         else:
    #             right[i] = right_val
    #     print("right :", right)

    #     res = 0
    #     for i in range(n):
    #         res += min(left[i],right[i]) - height[i]
    #     return res

if __name__ == '__main__':
    ob = Solution()
    res = ob.trap([1,0,2,0,1,0,3,1,0,2])
    print(res)


