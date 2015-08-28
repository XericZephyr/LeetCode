__author__ = 'clp'


class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        len_list = [len(s) for s in strs]
        min_len_index = len_list.index(min(len_list))
        needle = strs[min_len_index]
        if not needle:
            return needle
        all_match = False
        while not all_match and needle:
            all_match = True
            for s in strs:
                if not (s[:len(needle)] == needle):
                    all_match = False
                    needle = needle[:-1]
                    break
        return needle


if __name__ == "__main__":
    print Solution().longestCommonPrefix(['', '123', '12'])
    print Solution().longestCommonPrefix([])
    print Solution().longestCommonPrefix(['1231211', '123', '12'])
    print Solution().longestCommonPrefix(['123123', '123123', '123123'])