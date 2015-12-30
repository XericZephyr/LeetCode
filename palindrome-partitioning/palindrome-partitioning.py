


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        l = [[] for _ in range(1+len(s))]

        def is_palindrome(string):
            for i in range(len(string)/2):
                if string[i] != string[len(string)-1-i]:
                    return False
            return True

        def _dp(i):
            if not l[i]:
                if i == len(s):
                    l[i] = [[]]
                if i == len(s)-1:
                    l[i] = [[s[-1]]]
                for j in range(i, len(s)):
                    if is_palindrome(s[i:j+1]):
                        l[i] += [[s[i:j+1]] + r for r in _dp(j+1) if [s[i:j+1]] + r not in l[i]]
            return l[i]

        return list(_dp(0))

if __name__ == '__main__':
    print Solution().partition("aab")
    print Solution().partition("ab")
    print Solution().partition("aa")
    print Solution().partition("a")
    print Solution().partition("")
