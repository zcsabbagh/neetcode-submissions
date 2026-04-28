class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         # min time is O(n)
         # hash each int to a bucket
         # if any bucket has 2, return false immediately, else return true


        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

