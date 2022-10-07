from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    print("Sol :")

    low = 0
    high = len(nums)-1

    if len(nums) == 0:
        return [-1, -1]

    while (low < high):

        mid = (low) + ((high - low) // 2)

        print("mid :", mid, nums[5])

        if target > nums[mid]:
                low = mid + 1
        else:
            high = mid

        if target == nums[low]:
            i = nums.count(target)
            return [low, low+i-1]
        else:
            return [-1, -1]

            

nums = [5,7,7,8,8,10]
target = 8


# Output: [3,4]

res = searchRange(nums=nums,target=target)
print(res)