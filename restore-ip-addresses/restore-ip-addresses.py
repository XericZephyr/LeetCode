
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def op(k, start, end):
            if start > end:
                return []
            if k == 1:
                if s[start] == '0':
                    if start == end:
                        return [['0']]
                    else:
                        return []
                p = int(s[start:end+1])
                if 0 <= p <= 255:
                    return [[str(p)]]
                else:
                    return []
            else:
                ret = []
                for i in range(start+1, 1+min(start+3, end) if s[start] != '0' else start+2):
                    p = int(s[start:i])
                    if 0 <= p <= 255:
                        ret += [[str(p)] + l for l in op(k-1, i, end)]
                    else:
                        continue
                return ret
        if len(s) < 4:
            return []
        return ['.'.join(l) for l in op(4, 0, len(s)-1)]

if __name__ == '__main__':
    # print Solution().restoreIpAddresses("255255035")
    print Solution().restoreIpAddresses("0000")