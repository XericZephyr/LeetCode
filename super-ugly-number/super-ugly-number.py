


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 1:
            return 1
        k = len(primes)
        num_list = [1] * n
        max_idx = [0] * k
        max_list = [primes[i] * num_list[max_idx[i]] for i in range(k)]
        current_idx = 1
        while current_idx < n:
            min_idx = 0
            min_num = max_list[0]
            for i in range(1, k):
                if max_list[i] < min_num:
                    min_num = max_list[i]
                    min_idx = i
                elif max_list[i] == min_num:
                    max_idx[i] += 1
                    max_list[i] = primes[i] * num_list[max_idx[i]]
            num_list[current_idx] = min_num
            current_idx += 1
            max_idx[min_idx] += 1
            max_list[min_idx] = primes[min_idx] * num_list[max_idx[min_idx]]
        return num_list[-1]

if __name__ == '__main__':
    print Solution().nthSuperUglyNumber(1, [2,3,5])
    print Solution().nthSuperUglyNumber(12, [2,3,5])
    print Solution().nthSuperUglyNumber(12, [2, 7, 13, 19])
    print Solution().nthSuperUglyNumber(200, [2, 3])
    print Solution().nthSuperUglyNumber(20000, [2, 3])
    print Solution().nthSuperUglyNumber(100000,
         [7,19,29,37,41,47,53,59,61,79,83,89,101,103,109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251])
