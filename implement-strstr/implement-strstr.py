



class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if len(needle) == 1:
            for i in range(len(haystack)):
                if haystack[i] == needle:
                    return i

        def build_kmp_table(needle):
            T = [0] * len(needle)
            T[0] = -1
            pos, cnd = 2, 0
            while pos < len(needle):
                if needle[pos-1] == needle[cnd]:
                    cnd += 1
                    T[pos] = cnd
                    pos += 1
                elif cnd > 0:
                    cnd = 0
                else:
                    T[pos] = 0
                    pos += 1
            return T

        T = build_kmp_table(needle)

        m, i = 0, 0
        while m + i < len(haystack):
            if haystack[m+i] == needle[i]:
                if i == len(needle) - 1:
                    return m
                i += 1
            else:
                if T[i] > -1:
                    m += i - T[i]
                    i = T[i]
                else:
                    m += 1
                    i = 0
        return -1


if __name__ == '__main__':
    # print Solution().strStr("abccd", 'cd')
    print Solution().strStr("mississippi", "issip")



