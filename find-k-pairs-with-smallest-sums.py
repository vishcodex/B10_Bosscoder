from typing import List
import heapq

class Solution:

    # Solution 1 : timeout exception

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums2 or not nums1: return []
        heap = []
        heapq.heapify(heap)
        for i, num1 in enumerate(nums1[:k]):
            for num2 in nums2[:k//(i+1)]:
                print("num1+num2, num1, num2 :",  i, num1+num2, num1, num2)
                print("heap :", heap)
                print("num1+num2, num1, num2 :",  i, num1+num2, num1, num2)
                heapq.heappush(heap, [num1+num2, num1, num2])
        return [x[1:] for x in heapq.nsmallest(k, heap)]

    # Solution 2

    def kSmallestPairs(self, nums1, nums2, k):
        streams = map(lambda u: ([u+v, u, v] for v in nums2), nums1)
        stream = heapq.merge(*streams)
        return [suv[1:] for suv in itertools.islice(stream, k)]



res = Solution()

print(res.kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3))
        