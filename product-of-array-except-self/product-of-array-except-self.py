class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #
        #   cumproduct and then traverse from the reverse direction
        #
        out_list = [1] * len(nums)
        for i in range(len(nums)-1):
            out_list[i+1] = out_list[i] * nums[i]
        cum_product = 1
        for i in reversed(range(1, len(nums))):
            out_list[i] = out_list[i] * cum_product
            cum_product *= nums[i]
        out_list[0] = cum_product
        return out_list


if __name__ == '__main__':
    print Solution().productExceptSelf([1, 2, 3, 4])
    print Solution().productExceptSelf([5, 10, 15, 20])



