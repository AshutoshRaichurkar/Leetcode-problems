## Leetcode Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
## Solution Link: https://www.youtube.com/watch?v=cQ1Oz4ckceM

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r= 0, len(numbers)-1

        while l < r:

            stage = numbers[l] +numbers[r]

            if stage > target:
                r=r-1
            elif stage < target:
                l=l+1
            else:
                return [l+1,r+1]