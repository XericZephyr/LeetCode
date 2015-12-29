


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        def sort_counter():
            d = {}
            for i, c in enumerate(s):
                d[c] = d.get(c, 0) + 1
            return sorted(d.keys()), d

        skey, d = sort_counter()
        visit = {k: False for k in d}
        result = "0"
        for c in s:
            d[c] -= 1
            if visit[c]:
                continue
            while ord(c) < ord(result[-1]) and d[result[-1]] > 0:
                visit[result[-1]] = False
                result = result[:-1]
            result += c
            visit[c] = True
        return result[1:]






if __name__ == '__main__':
    # print Solution().removeDuplicateLetters("abababccc")
    # print Solution().removeDuplicateLetters("abdejianogeinantehahtheasedoafiosdjioaf")
    print Solution().removeDuplicateLetters("bcabc")

