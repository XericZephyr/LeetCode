


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for _ in range(1, n):
            ret = ""
            i = 0
            while i < len(s):
                pivot = s[i]
                c = 1
                for j in range(i+1, len(s)):
                    if s[j] != pivot:
                        break
                    c += 1
                if i == len(s) - 1:
                    ret += "1%s" % pivot
                    break
                else:
                    ret += "%d%s" % (c, pivot)
                    i += c
            s = ret
        return s

if __name__ == '__main__':
    for i in range(1, 50):
        print Solution().countAndSay(i)
