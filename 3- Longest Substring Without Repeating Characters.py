#Time Complexity: O(n*n)
#Space Compexity: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = 0;
        max_len = 0;
        
        while index < len(s):
            
            temp_len = 0;
            s_set = set(s);
            best_len = len(s_set);
            
            for i in range(index, len(s), +1):
                
                if(s[i] in s_set):
                    temp_len += 1;
                    max_len = max(max_len, temp_len);
                    s_set.remove(s[i]);
                    if(i == len(s)-1):
                        index +=1;
                    
            
                else:
                    index += 1;
                    break;
                                    
        return max_len;   
            