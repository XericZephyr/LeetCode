__author__ = 'clp'


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        str_list = ['' for x in range(numRows)]
        element_len = 2 * numRows - 2
        total_element = int(len(s)/element_len) + 1 if len(s) % element_len else int(len(s)/element_len)
        element_list = [s[i*element_len:(i+1)*element_len] for i in range(total_element)]
        for element in element_list:
            self.convert_single_element(element, str_list)
        return ''.join(str_list)

    def convert_single_element(self, sub_str, str_list):
        numRows = len(str_list)
        max_len = 2 * numRows - 2
        for index in range(len(sub_str)):
            if index < numRows:
                str_list[index] += sub_str[index]
            else:
                str_list[max_len-index] += sub_str[index]


if __name__ == '__main__':
    print Solution().convert("", 2)
    print Solution().convert("PAYPALISHIRING", 3)
    print Solution().convert("PAYPALISHIRING", 4)