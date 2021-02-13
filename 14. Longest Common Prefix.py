#Time Complexity: O(shortest word letters number * words number)
#Space Complexity: O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        index = 0
        
        if not strs:
            return output
        
        for letter in strs[0] :
            for i in strs:
                try:
                    if i[index] == letter:
                        continue;
                except:
                    return output
                
                else:
                    return output
            index += 1
            output += letter
                    
        return output
        