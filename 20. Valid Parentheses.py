#Time Complexity: O(n)
#Space Complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        char_dict = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        
        stack = []
        index = 0
        
        if not s:
            return True
        
        while index < len(s):
             
            if s[index] in char_dict:
                stack.append(s[index])
                
            else:
                if stack:
                    if char_dict[stack[-1]] == s[index]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            
            index += 1
        
        if stack:
            return False
        else:
            return True