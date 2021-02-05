#Time Complexity O(n)
#Space Complexity O(1)
class Solution
    def isPalindrome(self, x int) - bool
        if(x  0)
            return False
        else
            y = 0
            x_copy = x
            
            while(x  0)
                remain = x%10
                y = y  10 + remain 
                x = x10
                
            if(x_copy == y)
                return True
            else
                return False