#
# @lc app=leetcode id=1823 lang=python3
#
# [1823] Find the Winner of the Circular Game
#

# @lc code=start
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        index = 0
        arr = [ i for i in range(1, n+1)]
        size = len(arr)
        while size > 1:
            index = (index + k-1)%size
            del arr[index]
            size-=1
        return arr[0]
        
        
# @lc code=end

