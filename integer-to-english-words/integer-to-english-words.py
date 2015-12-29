

class Solution(object):
    num2word = {0: 'Zero', 1: 'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five',
                6:'Six', 7:'Seven', 8:'Eight', 9: 'Nine', 10: 'Ten',
                11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
                16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
                20: 'Twenty', 30: 'Thirty',40: 'Forty', 50: 'Fifty',
                60: 'Sixty', 70: 'Seventy',80: 'Eighty', 90: 'Ninety'}

    factor_words = ['Billion', 'Million', 'Thousand']
    factor = [1000000000, 1000000, 1000]

    def number1000ToWords(self, num):
        # we assert here, num <= 1000
        if num == 0:
            return ""
        ret = ""
        if num >= 100:
            ret += "%s %s " % (self.num2word[num/100], "Hundred")
            num %= 100
        if num >= 20:
            ret += "%s " % self.num2word[(num/10)*10]
            num %= 10
            if num:
                ret += "%s " % self.num2word[num]
        elif 1 <= num < 20:
            ret += "%s " % self.num2word[num]
        return ret.strip()

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            ret = "Negative "
            num = -num
        elif num > 0:
            ret = ""
        elif num == 0:
            return self.num2word[0]
        for i, factor in enumerate(self.factor):
            if num/factor > 0:
                ret += "%s %s " % (self.number1000ToWords(num/factor), self.factor_words[i])
                num %= factor
        if num:
            ret += self.number1000ToWords(num)
        return ret.strip()

if __name__ == '__main__':
    # for i in range(1, 101):
    #     print Solution().number1000ToWords(i)
    # print Solution().number1000ToWords(100)
    # print Solution().number1000ToWords(999)
    # print Solution().number1000ToWords(1)
    # print Solution().number1000ToWords(1)

    print Solution().numberToWords(123)
    print Solution().numberToWords(-123)
    print Solution().numberToWords(0)
    print Solution().numberToWords(1000)
    print Solution().numberToWords(2999)
