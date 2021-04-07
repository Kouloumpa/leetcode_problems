class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        special_roman_dict = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900   
        }
        
        symbol_list = list(s)
        result = 0
        
        while symbol_list:
            
            if len(symbol_list) >= 2 and symbol_list[0] + symbol_list[1] in special_roman_dict:
                
                result += special_roman_dict[symbol_list[0] + symbol_list[1]]
                symbol_list.pop(0)
                symbol_list.pop(0)
            
            elif symbol_list[0] in roman_dict:
                result += roman_dict[symbol_list[0]]
                symbol_list.pop(0)
        
        return result