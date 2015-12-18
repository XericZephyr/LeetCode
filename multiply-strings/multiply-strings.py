


        # def addition(num1, num2):
        #     M, N = len(num1), len(num2)
        #     if M > N:
        #         num2 = "0" * (M - N) + num2
        #     elif M < N:
        #         num1 = "0" * (N - M) + num1
        #     ret = ""
        #     c = 0
        #     for i, j in reversed(zip(num1, num2)):
        #         r = int(i) + int(j) + c
        #         c = r/10
        #         ret = str(r % 10) + ret
        #     if c:
        #         ret = '1' + ret
        #     return ret

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def addition(num1, num2):
            M, N = len(num1), len(num2)
            if N > M:
                M, N = N, M
                num1, num2 = num2, num1
            if num2 == "0":
                return num1
            ret = ""
            c = 0
            for i, j in reversed(zip(num1[-N:], num2)):
                r = int(i) + int(j) + c
                c = r/10
                ret = str(r % 10) + ret
            if c:
                if M == N:
                    ret = '1' + ret
                else:
                    ret = addition(num1[:-N], '1') + ret
            elif M > N:
                ret = num1[:-N] + ret
            return ret
        sign = 0
        if num1[0] == '-':
            num1 = num1[1:]
            sign += 1
        elif num1[0] == '+':
            num1 = num1[1:]
        if num2[0] == '-':
            num2 = num2[1:]
            sign += 1
        elif num2[0] == '+':
            num2 = num2[1:]
        M, N = len(num1), len(num2)
        if M < N:
            M, N = N, M
            num1, num2 = num2, num1

        h = {"0": "0", "1": num1}
        ret = "0"
        for i in range(N):
            last_digit = num2[N - i - 1]
            if last_digit not in h:
                s = "0"
                for j in range(int(last_digit)):
                    s = addition(s, num1)
                h[last_digit] = s
            ret = addition(ret, h[last_digit] + "0" * i)
        return ret if sign % 2 == 0 or ret == '0' else "-" + ret

if __name__ == '__main__':
    # print Solution().multiply("1", "2")
    print Solution().multiply("3", "5")
    print Solution().multiply("6", "6")
    print Solution().multiply("500", "6")
    # print Solution().multiply("0", "6")
    # print Solution().multiply("6", "0")
    # print Solution().multiply("0", "0")
    # print Solution().multiply("-1", "0")
    # print Solution().multiply("-1", "2")
    # print Solution().multiply("-1", "-2")
    print Solution().multiply("7832975372897352", "23685265689235729873")


