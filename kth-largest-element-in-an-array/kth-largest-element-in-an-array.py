


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def find_largest_k(nums, start, end, k):

            def partition(nums, start, end):
                pivot = nums[end]
                i = start
                for j in range(start, end):
                    if nums[j] >= pivot:
                        nums[i], nums[j] = nums[j], nums[i]
                        i += 1
                nums[i], nums[end] = nums[end], nums[i]
                return i

            p = partition(nums, start, end)
            if p == k:
                return nums[k]
            elif p < k:
                return find_largest_k(nums, p+1, end, k)
            else:
                return find_largest_k(nums, start, p-1, k)

        return find_largest_k(nums, 0, len(nums)-1, k-1)


if __name__ == '__main__':
    print Solution().findKthLargest([1,2,3,4,5,6], 2)
    print Solution().findKthLargest([1,2,3,4,5,7], 2)
    print Solution().findKthLargest([1,2,3,4,7], 2)
    print Solution().findKthLargest([1,2,7], 2)
    print Solution().findKthLargest([1], 2)



