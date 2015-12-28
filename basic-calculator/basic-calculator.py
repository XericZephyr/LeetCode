class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        def shunting_yard(expr):
            """
            :param expr: expression in str
            :return: reverse polish notation, in list
            """

            class ExprStream(object):

                def __init__(self, expr):
                    self._expr = expr
                    self._cursor = 0
                    self._last_token = ''

                def reset(self):
                    self._cursor = 0

                def read_next_token(self):
                    if self._cursor >= len(self._expr):
                        raise StopIteration
                    if ord('0') <= ord(self._expr[self._cursor]) <= ord('9'):
                        num_cursor = self._cursor
                        while num_cursor < len(self._expr) and \
                                ord('0') <= ord(self._expr[num_cursor]) <= ord('9'):
                            num_cursor += 1
                        ret = int(self._expr[self._cursor:num_cursor])
                        self._cursor = num_cursor
                    elif self._expr[self._cursor] in [' ', '\t']:
                        while self._cursor < len(self._expr) and \
                                self._expr[self._cursor] in [' ', '\t']:
                            self._cursor += 1
                        ret = self.read_next_token()
                    elif self._expr[self._cursor] in ['+', '(', ')']:
                        self._cursor += 1
                        ret = self._expr[self._cursor - 1]
                    elif self._expr[self._cursor] == '-':
                        if self._last_token in ['+', '(', '']:
                            self._cursor += 1
                            ret = -self.read_next_token()
                        else:
                            ret = '-'
                            self._cursor += 1
                    self._last_token = ret
                    return ret

                def __iter__(self):
                    return self

                def next(self):
                    return self.read_next_token()

                def __next__(self):
                    # for python 3.0 capability
                    return self.next()

            op = []
            rpn = []
            for token in ExprStream(expr):
                if isinstance(token, int):
                    rpn.append(token)
                elif isinstance(token, (str, unicode)):
                    if token in ['+', '-']:
                        while op and op[-1] in ['+', '-']:
                            rpn.append(op.pop())
                        op.append(token)
                    elif token == '(':
                        op.append(token)
                    elif token == ')':
                        while op[-1] != '(':
                            rpn.append(op.pop())
                        op.pop()
            while op:
                rpn.append(op.pop())

            return rpn

        def evaluate_rpn(rpn):
            op = {'+': lambda x, y: x + y,
                  '-': lambda x, y: x - y}
            num_stack = []
            for token in rpn:
                if isinstance(token, int):
                    num_stack.append(token)
                elif isinstance(token, (str, unicode)) and token in op.keys():
                    b = num_stack.pop()
                    a = num_stack.pop()
                    num_stack.append(op[token](a, b))
            return num_stack[-1]

        rpn = shunting_yard(s)
        return evaluate_rpn(rpn)

if __name__ == '__main__':
    # print Solution().calculate("(15+(4 +5+2)-3)+(6+8)")
    # print Solution().calculate("1   + 1")
    # print Solution().calculate(" 2-1 + 2 ")
    # print Solution().calculate("(1+(4+5+2)-3)+(6+8)")
    # print Solution().calculate("0")
    print Solution().calculate("-15")
    print Solution().calculate("2+-5")
    print Solution().calculate("2+(-15)")
    # print Solution().calculate("  ")
