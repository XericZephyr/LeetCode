

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        else:
            ugly_list = [1]
            ugly_factor = [2, 3, 5]
            ugly_idx_list = [0] * len(ugly_factor)
            for _ in range(n-1):
                new_ugly_list = [ugly_list[idx]*f for f, idx in zip(ugly_factor, ugly_idx_list)]
                new_ugly = min(new_ugly_list)
                for idx, new_num in enumerate(new_ugly_list):
                    if new_num == new_ugly:
                        ugly_idx_list[idx] += 1
                ugly_list.append(new_ugly)
            return ugly_list[-1]


if __name__ == '__main__':
    for i in range(1, 11):
        print Solution().nthUglyNumber(i)
    print Solution().nthUglyNumber(7)
