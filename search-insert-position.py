def searchInsert(self, nums: List[int], target: int) -> int:

    # Brute force approach
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] >= target:
                return i

    # o(log n)

        if target < nums[0]:
                return 0
        elif target > nums[-1]:
            return len(nums)
        left = 0
        right = len(nums) - 1
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        while left < right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle
        if nums[left] > target:
            return left
        else:
            return left + 1
        