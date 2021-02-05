#Time Complexity: O(n)
#Space Complexity: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
    
        def getArea(start_point: List[int], end_point: List[int]) -> int:
            return min(start_point[1], end_point[1]) * (end_point[0] - start_point[0])
        
        start = 0
        end  = len(height) - 1
        best = 0
        
        while start != end:
            x1 = [start, height[start]]
            x2 = [end, height[end]]
            x = getArea(x1, x2)
            if x > best:
                best = x
            if(height[start] > height[end]):
                end -= 1
            else:
                start += 1
                
        return best
        