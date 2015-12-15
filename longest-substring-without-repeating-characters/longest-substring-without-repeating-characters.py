

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_occurance = {}
        start, end = 0, 0
        max_length = 0
        for i, c in enumerate(s):
            if c not in last_occurance:
                last_occurance[c] = i
            else:
                end = i - 1
                new_length = end - start + 1
                start = max(last_occurance[c] + 1, start)
                last_occurance[c] = i
                max_length = max(new_length, max_length)

            if i == len(s) - 1:
                new_length = i - start + 1
                max_length = max(new_length, max_length)

        return len(s) if max_length == 0 else max_length

if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring("abcabcbb")
    print Solution().lengthOfLongestSubstring("bbbbbb")

    print Solution().lengthOfLongestSubstring("")
    print Solution().lengthOfLongestSubstring("a")
    #
    print Solution().lengthOfLongestSubstring("aab")
    print Solution().lengthOfLongestSubstring("tmmzuxt")