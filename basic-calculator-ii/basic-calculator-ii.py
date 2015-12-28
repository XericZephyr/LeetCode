


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # only consider +, -, *, /, no bracket

        class ExprStream(object):

            def __init__(self, expr):
                self._expr = expr
                self._cursor = 0
                self._last_token = ''

            def read_next_token(self):
                if self._cursor >= len(self._expr):
                    raise StopIteration
                if ord('0') <= ord(self._expr[self._cursor]) <= ord('9'):
                    num_cursor = self._cursor
                    while num_cursor < len(self._expr) and \
                            ord('0') <= ord(self._expr[num_cursor]) <= ord('9'):
                        num_cursor += 1
                    token = int(self._expr[self._cursor:num_cursor])
                    self._cursor = num_cursor
                elif self._expr[self._cursor] in ['+', '-', '*', '/']:
                    token = self._expr[self._cursor]
                    self._cursor += 1
                elif self._expr[self._cursor] in [' ', '\t']:
                    while self._cursor < len(self._expr) and \
                                self._expr[self._cursor] in [' ', '\t']:
                        self._cursor += 1
                    token = self.read_next_token()
                else:
                    raise Exception("Unknown Token")

                self._last_token = token
                return token

            def __iter__(self):
                return self

            def next(self):
                return self.read_next_token()

            def __next__(self):
                return self.next()

        def shunting_yard(expr):
            op = []
            rpn = []
            for token in ExprStream(expr):
                if isinstance(token, int):
                    rpn.append(token)
                elif isinstance(token, (str, unicode)):
                    if token in ['+', '-']:
                        while op and op[-1] in ['+', '-', '*', '/']:
                            rpn.append(op.pop())
                        op.append(token)
                    elif token in ['*', '/']:
                        while op and op[-1] in ['*', '/']:
                            rpn.append(op.pop())
                        op.append(token)
            while op:
                rpn.append(op.pop())
            return rpn

        def evaluate_rpn(rpn):
            op = {
                '+': lambda x, y: x+y,
                '-': lambda x, y: x-y,
                '*': lambda x, y: x*y,
                '/': lambda x, y: x/y
            }
            num_stack = []
            for token in rpn:
                if isinstance(token, int):
                    num_stack.append(token)
                elif isinstance(token, (str, unicode)):
                    b = num_stack.pop()
                    a = num_stack.pop()
                    num_stack.append(op[token](a, b))
            return num_stack[-1]

        return evaluate_rpn(shunting_yard(s))

if __name__ == '__main__':
    print Solution().calculate("3+2*2")
    print Solution().calculate(" 3/2 ")
    print Solution().calculate(" 3+5 / 2 ")
    print Solution().calculate("0")
    print Solution().calculate(" 0 / 5 ")
    print Solution().calculate(" 0 / 5 ")