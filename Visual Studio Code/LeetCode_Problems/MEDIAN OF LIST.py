class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        num = nums1 + nums2
        num.sort()
        nums = num
        if len(nums) % 2 == 1:
            return nums[(int((len(nums) / 2)) + 1) - 1]
        else:
            return (
                nums[int(((len(nums) / 2)) - 1)] + nums[int(((len(nums) / 2) + 1) - 1)]
            ) / 2


o = Solution()
print(
    o.findMedianSortedArrays(
        [1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    )
)
