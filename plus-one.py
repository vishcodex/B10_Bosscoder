from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = int("".join([str(x) for x in digits]))
        digits += 1
        return list(str(digits))



    def plusOne(self, digits: List[int]) -> List[int]:
        lastDigit = len(digits) - 1
        
        if len(digits) == 1:
            if digits[0] == 9:
                digits[0] = 1
                digits.append(0)
                
            else:
                digits[0] += 1
            
            return digits
        
        while lastDigit >= 0:
            if digits[lastDigit] != 9:
                digits[lastDigit] += 1
                return digits
            
            digits[lastDigit] = 0
            lastDigit -= 1
            
        digits[0] = 1
        digits.append(0)
        return digits
        