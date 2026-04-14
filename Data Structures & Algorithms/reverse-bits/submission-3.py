
class Solution:
    def reverseBits(self, n: int) -> int:
        bits = list(bin(n))[2:]
        zeroes = ["0"] * (32 - len(bits))
        final = zeroes + bits

        return int("".join(reversed(final)), 2)
