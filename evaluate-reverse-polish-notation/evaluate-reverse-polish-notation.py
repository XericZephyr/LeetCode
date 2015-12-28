


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        op = {
            '+': lambda x, y: x+y,
            '-': lambda x, y: x-y,
            '*': lambda x, y: -(abs(x)*abs(y)) if x*y < 0 else abs(x)*abs(y),
            '/': lambda x, y: -(abs(x)/abs(y)) if x*y < 0 else abs(x)/abs(y)
        }
        num_list = []
        for t in tokens:
            if t in op.keys():
                a = num_list.pop()
                b = num_list.pop()
                num_list.append(op[t](b, a))
            else:
                num_list.append(int(t))
        return num_list[-1]

if __name__ == '__main__':
    print Solution().evalRPN(["2", "1", "+", "3", "*"])
    print Solution().evalRPN(["4", "13", "5", "/", "+"])
    print Solution().evalRPN(["0","3","/"])
    print Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])