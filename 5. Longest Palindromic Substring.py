#Time Complexity: O(n*n)
#Space Complexity: O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = "";
        for i in range(len(s)):
            for j in range(len(s), i , -1):
                if len(palindrome) >= j-i:
                    break;
                elif s[i:j] == s[i:j][::-1]:
                    palindrome = s[i:j];
                    break;
        return palindrome;