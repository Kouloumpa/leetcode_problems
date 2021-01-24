#Time Complexity: O(n)
#Space Compexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index1 = [(num , indx) for indx  , num in enumerate(nums)];
        index1.sort
        start , end = 0, len(nums)-1;
        while start < end :
            current = index1[start][0] + index1[end][0];
            if current < target:
                start += 1;
            elif current > target:
                end -=1;
            else:
                return [index1[start][1], index1[end][1]];
