class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
        else: 
            carry = True
            i = len(digits)-1
            while carry and i >= 0: 
                if digits[i] != 9:
                    digits[i] += 1
                    carry = False
                else: digits[i] = 0
                i -= 1
            if carry == True: 
                digits.insert(0,1)
        return digits
            