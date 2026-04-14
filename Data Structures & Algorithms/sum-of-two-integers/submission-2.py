
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # saw_negative = False
        # if a < 0: 
        #     a = (abs(a) ^ 2047) + 1
        #     saw_negative = True
        #     print(a)
        # if b < 0: 
        #     b = (abs(b) ^ 2047) + 1
        #     saw_negative = True
        #     print(b)
        # length_max = max(math.ceil(math.log(a, 2))+1, math.ceil(math.log(b, 2))+1)
        # print(length_max)
        # bit_a = bin(a)[2:].zfill(length_max)
        # bit_b = bin(b)[2:].zfill(length_max)
        # print(bit_b)
        # print(bit_a)
        # carry = False
        # result = ["0"] * length_max
        # print(result)
        # for i in range(len(bit_a)-1, -1, -1):
        #     ba = bit_a[i]
        #     bb = bit_b[i]
        #     r = 1 if carry else 0 
        #     carry = False
        #     if bb == ba: 
        #         if bb == "1": 
        #             carry = True 
        #         result[i] = str(r)
        #     else: 
        #         if r == 1:
        #             carry = True
        #             result[i] = "0"
        #         else: 
        #             result[i] = "1"
        # if carry and not saw_negative: 
        #     result.insert(0, "1")
        # print(result)
        # print("".join(result))

        # return int("".join(result),2) ^ 2047
        MAX_INT = 0x7FFFFFFF    #  2147483647, biggest 32-bit positive int
        MASK = 0xFFFFFFFF       #  32 bits of 1s: for simulating overflow

        while b != 0:
            carry = (a & b) & MASK         # calculate carry
            a = (a ^ b) & MASK             # add without carry
            b = (carry << 1) & MASK        # move carry to the next higher bit

        # If a is bigger than max signed int, it's actually a negative number
        return a if a <= MAX_INT else ~(a ^ MASK)