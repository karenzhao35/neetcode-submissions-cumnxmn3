
class Solution:
    def reverseBits(self, n: int) -> int:
        bits = list(bin(n))[2:]
        bits = ["0"] * (32 - len(bits)) + bits
        return int("".join(reversed(bits)), 2)
