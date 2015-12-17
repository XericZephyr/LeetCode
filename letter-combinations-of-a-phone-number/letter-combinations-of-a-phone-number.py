


class Solution(object):
    num2letter = {'2': "abc", '3': "def", '4': 'ghi', '5': 'jkl',
                  '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
                  '1': '*', '*': '*', '#': '#'}
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return list(self.num2letter[digits])
        elif len(digits) > 1:
            return [c + r for c in self.num2letter[digits[0]]
                    for r in self.letterCombinations(digits[1:])]

if __name__ == '__main__':
    print Solution().letterCombinations("23")
