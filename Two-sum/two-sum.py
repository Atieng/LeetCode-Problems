class Solution:
    def twoSum(self, nums, target):
        index_dict={}
        for i, num in enumerate(nums):
            complement = target-nums
            if complement in index_dict:
                return [index_dict[complement],i]
            
            index_dict[num]=i