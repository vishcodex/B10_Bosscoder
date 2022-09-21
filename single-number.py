from typing import List


def singleNumber(nums: List[int]) -> int:
    ans = 0
    for i in nums:
        print(ans, i)
        ans = ans ^ i
        print("ans is :", ans)
    return ans



nums = [2,2,1,1,3]
res = singleNumber(nums=nums)
print(res)