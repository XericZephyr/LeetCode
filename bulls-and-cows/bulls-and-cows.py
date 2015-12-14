

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = 0
        B = 0
        secret_h = [0] * 10
        guess_h = [0] * 10
        for i, j in zip(list(secret), list(guess)):
            if i == j:
                A += 1
            else:
                secret_h[int(i)] += 1
                guess_h[int(j)] += 1
        for i, j in zip(secret_h, guess_h):
            B += min((i, j))
        return "%dA%dB" % (A, B)


if __name__ == '__main__':
    print Solution().getHint("1123", "0111")
    print Solution().getHint("1807", "7810")


