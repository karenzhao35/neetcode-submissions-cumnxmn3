class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = {}
        res = 0
        if not nums: return 0

        for num in nums: 
            if num in seq: 
                continue
            
            if num-1 in seq: 
                prev_seq = seq[num-1]
                new_seq = prev_seq + 1
                seq[num] = new_seq
                begin_ind = num - new_seq
                seq[begin_ind] = new_seq

            if num+1 in seq: 
                if num not in seq: seq[num] = 0
                end_ind = seq[num+1] + num+1
                begin_ind = num - seq[num]

                new_range = seq[num+1] + seq[num] + 1
                seq[begin_ind] = new_range
                seq[end_ind] = new_range

            
            if num not in seq: 
                seq[num] = 0
            print(seq)
            res = max(seq.values())
        return res+1