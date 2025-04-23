class Solution:
    def reverse(self, x: int) -> int:
        str1 = str(x)
        if "-" in str1:
            str1 = "-" + str1[len(str1) - 1 : 0 : -1]
        elif str1[len(str1) - 1] == 0:
            str1 = str1[len(str1) - 2 :: -1]
        else:
            str1 = str1[::-1]
        if (int(str1) <= 2147483647) and (int(str1) >= -2147483648):
            return int(str1)

        else:
            return 0


o = Solution()
print(o.reverse(1534236469))
