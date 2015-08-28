__author__ = 'clp'


class Solution(object):

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        def build_alpha_table(word):
            # assume we only have lowercase alphabets
            alpha_hash_table = [0] * 26
            for c in word:
                alpha_hash_table[ord(c)-ord('a')] += 1
            return alpha_hash_table

        def compare_alpha_table(tableA, tableB):
            # return True if equal, otherwise False
            if not (len(tableA) == len(tableB)):
                return False

            return reduce(lambda x, y: x and (y[0] == y[1]), zip(tableA, tableB), True)

        return compare_alpha_table(build_alpha_table(s), build_alpha_table(t)) if len(s) == len(t) else False


if __name__ == '__main__':
    print Solution().isAnagram("anagram", "nagaram")
    print Solution().isAnagram("rat", "car")
    print Solution().isAnagram("rat", "")
    print Solution().isAnagram("", "")

