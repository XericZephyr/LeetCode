

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        class PathStream(object):

            def __init__(self, abs_path):
                self._abs_path = abs_path
                self._cursor = 0

            def read_next_token(self):
                if self._cursor >= len(self._abs_path):
                    raise StopIteration
                if self._abs_path[self._cursor] == '/':
                    self._cursor += 1
                    ret = self.read_next_token()
                else:
                    path_cursor = self._cursor
                    while path_cursor < len(self._abs_path) and \
                                    self._abs_path[path_cursor] != '/':
                        path_cursor += 1
                    ret = self._abs_path[self._cursor:path_cursor]
                    self._cursor = path_cursor
                return ret

            def __iter__(self):
                return self

            def next(self):
                return self.read_next_token()

            def __next__(self):
                return self.next()

        ret = []
        for token in PathStream(path):
            if token == '.':
                continue
            elif token == '..':
                if ret:
                    ret.pop()
            else:
                ret.append(token)
        return "/" + '/'.join(ret)


if __name__ == '__main__':
    # print Solution().simplifyPath("/a/./b/../../c/")
    # print Solution().simplifyPath("/home/")
    # print Solution().simplifyPath("/")
    # print Solution().simplifyPath("./")
    # print Solution().simplifyPath("/")
    print Solution().simplifyPath("/../")
    print Solution().simplifyPath("/.")
    print Solution().simplifyPath("/..")


