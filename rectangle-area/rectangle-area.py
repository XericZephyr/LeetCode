


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        total_area = (H-F) * (G-E) + (D-B)*(C-A)
        H, W = (min(D, H) - max(B, F)), (min(C, G) - max(A, E))
        if H > 0 and W > 0:
            return total_area - H * W
        else:
            return total_area
        # if (D-B) * (C-A) == 0:
        #     return (H-F) * (G-E)
        # elif (H-F) * (G-E) == 0:
        #     return (D-B)*(C-A)
        # elif E <= A < C <= G and F <= B < D <= H:
        #     return (H-F) * (G-E)
        # elif A <= E < G <= C and B <= F < H <= D:
        #     return (D-B) * (C-A)
        # elif E <= A <= G:
        #     if F <= B <= H:
        #         return total_area - (H-B) * (G-A)
        #     elif F <= D <= H:
        #         return total_area - (D-F) * (G-A)
        # elif E <= C <= G:
        #     if F <= B <= H:
        #         return total_area - (C-E) * (H-B)
        #     elif F <= D <= H:
        #         return total_area - (D-F) * (C-E)
        # else:
        #     return total_area

if __name__ == '__main__':
    print Solution().computeArea(0,0,0,0,-1,-1,1,1)
    print Solution().computeArea(-2,-2,2,2,3,3,4,4)
    print Solution().computeArea(-2,-2,2,2,-3,-3,3,-1)
