class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
            
        max_sum = nums[0]
        sub_array = nums[0]
            
        for num in nums[1:]:
                
            sub_array = max(num, sub_array + num)
            max_sum = max(max_sum , sub_array)
                
        return max_sum