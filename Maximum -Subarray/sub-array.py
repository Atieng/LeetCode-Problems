class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # INitializze the maximum sum so far
        max_sum =nums[0]
        # The outer loop of the sub array
        for i in range(len(nums)):
            sum_of_subarray = 0
            for j in range(i, len(nums)):
                sum_of_subarray = sum_of_subarray +nums[j]
                max_sum =max(max_sum,sum_of_subarray)

        return max_sum
    
sol = Solution()
nums =[-2, -3, 0,4, 6,2]
print(sol.maxSubArray(nums))

