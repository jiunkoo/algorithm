#
# @lc app=leetcode id=2035 lang=python3
#
# [2035] Partition Array Into Two Arrays to Minimize Sum Difference
#

# @lc code=start
from typing import List

class Solution:
    def minimumDifference(self, nums):
        n = len(nums)
        half = n // 2
        total = sum(nums)

        left, right = nums[:half], nums[half:]

        def get_sums(arr):
            res = [[] for _ in range(len(arr) + 1)]

            def dfs(i, cnt, acc):
                if i == len(arr):
                    res[cnt].append(acc)
                    return

                dfs(i + 1, cnt, acc)
                dfs(i + 1, cnt + 1, acc + arr[i])

            dfs(0, 0, 0)
            return res

        left_sums = get_sums(left)
        right_sums = get_sums(right)

        for lst in right_sums:
            lst.sort()

        def lower_bound(arr, target):
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        ans = float("inf")

        for size in range(len(left_sums)):
            for s in left_sums[size]:
                need = half - size
                if 0 <= need < len(right_sums):
                    arr = right_sums[need]
                    target = total / 2 - s
                    idx = lower_bound(arr, target)

                    for j in [idx, idx - 1]:
                        if 0 <= j < len(arr):
                            picked = s + arr[j]
                            diff = abs(2 * picked - total)
                            if diff < ans:
                                ans = diff

        return ans
# @lc code=end
