# Given two arrays of integers with equal lengths, return the maximum value of:

# |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

# where the maximum is taken over all 0 <= i, j < arr1.length.

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
	# store the value of each 4 combination
        l1, l2, l3, l4 = [] , [], [], []
       
	   # use formula
        for i in range(len(arr1)):
            l1.append(i + arr1[i] + arr2[i])
            l2.append(i - arr1[i] + arr2[i])
            l3.append(i - arr1[i] - arr2[i])
            l4.append(i + arr1[i] - arr2[i])
            
        maximum_absolute_difference = 0
		# required maximum absolute difference is maximum-minimum of 4 combinations 
        maximum_absolute_difference = max(maximum_absolute_difference, max(l1) - min(l1))
        maximum_absolute_difference= max(maximum_absolute_difference, max(l2) - min(l2))
        maximum_absolute_difference= max(maximum_absolute_difference, max(l3) - min(l3))
        maximum_absolute_difference= max(maximum_absolute_difference, max(l4) - min(l4))
        
        
        return maximum_absolute_difference
        

if __name__ == '__main__':
    os = Solution()
    res = os.maxAbsValExpr([1,2,3,4],[-1,4,5,6])
    print(res)