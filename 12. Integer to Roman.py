#Time Complexity: O(n)
#Space Complexity: O(1)
class Solution:
    def intToRoman(self, num: int) -> str:
        output = ''
        while num - 1000 >= 0:
            output += "M"
            num -= 1000
        
        while num - 500 >= 0:
            if 900 <= num < 1000:
                output += "CM"
                num -= 900
                continue
            output += "D"
            num -= 500
            
        while num - 100 >= 0 :
            if 400 <= num < 500:
                output += "CD"
                num -= 400
                continue
            output += "C"
            num -= 100
            
        while num - 50 >= 0 :
            if 90 <= num < 100:
                output += "XC"
                num -= 90
                continue
            output += "L"
            num -= 50
            
        while num -10 >= 0 :
            if 40 <= num < 50:
                output += "XL"
                num -= 40
                continue
            output += "X"
            num -= 10
        
        while num -5 >= 0 :
            if 9 <= num < 10:
                output += "IX"
                num -= 9
                continue
            output += "V"
            num -= 5
            
        while num -1 >= 0 :
            if 4 <= num < 5:
                output += "IV"
                num -= 4
                continue
            output += "I"
            num -= 1    
        
        return output