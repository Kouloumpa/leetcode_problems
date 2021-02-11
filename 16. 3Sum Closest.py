#Time Complexity: O(n*n)
#Space Complexity: O(n)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        min_diff = float(inf)
        start = 0
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                cur_sum = nums[i] + nums[start] + nums[end]
                if abs(target - cur_sum) < abs(target - min_diff):
                    min_diff = cur_sum
                if cur_sum < target:
                    start += 1
                else:
                    end -= 1
        return min_diff