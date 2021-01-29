#Time Complexity: O(n)
#Space Complexity: O(1)
class Solution:
    def reverse(self, x: int) -> int:
         if x < 0 :
            y = -1 * int(str(x)[::-1]);
            if(abs(y) <= (2 ** 31)):
                y *= -1;
                return y;
            else:
                return 0;
        
        else:
            y = int(str(x)[::-1]);
            if(abs(y) <= (2 ** 31 - 1)):
                return y;
            else:
                return 0;