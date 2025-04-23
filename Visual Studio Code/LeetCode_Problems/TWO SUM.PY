class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lst = []
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        lst.append([i, j])
                    else:
                        pass
        # print(lst)
        if len(lst) > 1:
            del lst[1:]
        lst1 = lst[0]
        lst1.sort()
        return lst1


o = Solution()
print(o.twoSum([3, 2, 4, 1], 6))
