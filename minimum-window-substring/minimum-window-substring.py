


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        h = {c: 0 for c in s}
        for c in t:
            h[c] = h.get(c, 0) + 1
        counter = len(t)
        begin = end = 0
        d = 0xFFFFFFFF
        while end < len(s):
            if h[s[end]] > 0:
                counter -= 1
            while counter == 0:
                if end-begin+1 < d:
                    head = begin
                    d = end-begin+1
                if h[s[begin]] >= 0:
                    counter += 1
                h[s[begin]] += 1
                begin += 1
            h[s[end]] -= 1
            end += 1
        return s[head:head+d] if d < 0xFFFFFFFF else ""

if __name__ == '__main__':
    print Solution().minWindow("ADOBECODEBANC", "ABC")