

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        word_list = str.split(' ')
        pattern_list = list(pattern)
        if not (len(word_list) == len(pattern_list)):
            return False
        word2pat_dict = {}
        pat2word_dict = {}
        for k, v in zip(word_list, pattern_list):
            if k in word2pat_dict:
                if not (v == word2pat_dict[k]):
                    return False
            elif v in pat2word_dict:
                if not (k == pat2word_dict[v]):
                    return False
            else:
                pat2word_dict[v] = k
                word2pat_dict[k] = v
        return True

if __name__ == '__main__':
    print Solution().wordPattern("abba", "dog cat cat dog")
    print Solution().wordPattern("abba", "dog cat cat fish")
    print Solution().wordPattern("aaaa", "dog cat cat dog")
    print Solution().wordPattern("abba", "dog dog dog dog")
    print Solution().wordPattern("abb", "dog dog dog dog")