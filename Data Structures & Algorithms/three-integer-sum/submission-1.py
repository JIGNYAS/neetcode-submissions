class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()

        for k, val in enumerate(nums):
            if k > 0 and val == nums[k-1]:
                continue
            
            i,j = k+1,len(nums)-1
            while i < j:
                threesum = val + nums[i] + nums[j]
                if threesum > 0:
                    j -= 1
                elif threesum < 0:
                    i += 1
                else:
                    sol.append([val, nums[i], nums[j]])
                    i += 1
                    while nums[i] == nums[i-1] and i < j:
                        i += 1
        return sol



        

        