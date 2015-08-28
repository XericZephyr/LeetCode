__author__ = 'clp'


class Solution(object):


    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        p1, p2 = m-1, n-1
        pm = m+n-1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] <= nums2[p2]:
                nums1[pm] = nums2[p2]
                p2 -= 1
            else:
                nums1[pm] = nums1[p1]
                p1 -= 1
            pm -= 1
        if p2 >= 0:
            for i in range(p2+1):
                nums1[i] = nums2[i]

if __name__ == "__main__":
    n2 = [2, 3, 7]
    n1 = [1, 5, 6] + [0 for i in range(len(n2))]
    print n1
    Solution().merge(n1 , len(n1)-len(n2), n2, len(n2))
    print n1

    n2 = []
    n1 = [1] + [0 for i in range(len(n2))]
    print n1
    Solution().merge(n1 , len(n1)-len(n2), n2, len(n2))
    print n1

    n2 = [1]
    n1 = [] + [0 for i in range(len(n2))]
    print n1
    Solution().merge(n1 , len(n1)-len(n2), n2, len(n2))
    print n1

    n2 = []
    n1 = [] + [0 for i in range(len(n2))]
    print n1
    Solution().merge(n1 , len(n1)-len(n2), n2, len(n2))
    print n1

    n2 = [1, 2, 3]
    n1 = [4, 5, 7] + [0 for i in range(len(n2))]
    print n1
    Solution().merge(n1 , len(n1)-len(n2), n2, len(n2))
    print n1

    n2 = [4, 5, 7]
    n1 = [1, 2, 3] + [0 for i in range(len(n2))]
    print n1
    Solution().merge(n1 , len(n1)-len(n2), n2, len(n2))
    print n1




