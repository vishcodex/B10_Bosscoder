
from typing import List

def search(self, nums: List[int], target: int) -> int:
    # left pointer
    start=0  
    # right pointer
    end=len(nums)-1
    # until both comes not equal
    while start<=end:
        mid=(start+end)>>1      # Calculating mid point
        # checking if mid is target then return  index
        if nums[mid]==target:
            return mid
        #   checking first half array is sorted or not
        elif nums[mid]>=nums[start]:
            # checking target is exist in first half or not
            if (target>=nums[start] and target<nums[mid]):
                end=mid-1
            else:
                start=mid+1
        else:
            # checking for target exist in second half or not
            if (target<=nums[end] and target>nums[mid]):
                start=mid+1
            else:
                end=mid-1
    return -1


nums = [4,5,6,7,0,1,2]
target = 0
res = search(nums=nums,target=target)
print(res)