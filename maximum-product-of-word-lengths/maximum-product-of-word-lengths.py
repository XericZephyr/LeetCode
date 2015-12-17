




class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def hash_word(word):
            ret = 0
            for c in word:
                ret |= (1 << (ord(c) - ord('a')))
            return ret

        N = len(words)
        if N < 2:
            return 0
        h = [hash_word(word) for word in words]
        max_length = 0
        for i in range(N-1):
            for j in range(i, N):
                if (h[i] & h[j]) == 0:
                    max_length = max(max_length, len(words[i]) * len(words[j]))
        return max_length

if __name__ == '__main__':
    print Solution().maxProduct(["a", "aa", "aaa", "aaaa"])
    print Solution().maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"])
    print Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
