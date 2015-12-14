

class Solution(object):

    acgt_map = {'A': 0, 'C': 1, 'T': 2, 'G': 3}

    def ten_digit_hash(self, s):
        assert len(s) >= 10
        prev_bit = reduce(lambda x, y: (x << 2) | y, [self.acgt_map[c] for c in s[:10]], 0)
        current = 10
        hash_table = [prev_bit]
        while current < len(s):
            prev_bit = (prev_bit << 2 & 0xFFFFF) | self.acgt_map[s[current]]
            hash_table.append(prev_bit)
            current += 1
        return hash_table

    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) <= 10:
            return []
        hash_table = self.ten_digit_hash(s)
        counter = {}
        result = []
        for i, num in enumerate(hash_table):
            counter[num] = counter.get(num, 0) + 1
            if counter[num] == 2:
                result.append(s[i:i+10])
        return result



if __name__ == '__main__':
    print Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
    print Solution().findRepeatedDnaSequences("")
