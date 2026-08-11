class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         d = {}
         for i in range(len(nums)):
            ans = target - nums[i]
            if(ans in d):
                return list((d[ans],i))
            else:
                d[nums[i]] = i
        


        