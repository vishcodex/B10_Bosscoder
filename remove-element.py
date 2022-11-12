class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i]==val:
                continue
            # print(k, nums[k], nums[i])
            nums[k] =nums[i]
            k+=1
        return k
        