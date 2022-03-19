class Solution:
    def find_no_pairs_less(self, sum , nums):
        pointer1 = 0
        pointer2 = 1
        ans = 0
        while pointer1 != len(nums)-1:
            if pointer2 == len(nums):
                ans += pointer2-pointer1-1
                pointer1+=1
            else :
                if nums[pointer2] - nums[pointer1] <= sum:
                    pointer2+=1
                else:
                    ans +=pointer2-pointer1-1
                    pointer1+=1
        return ans

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_ = 0
        max_ = max(nums)-min(nums)
        while min_<max_:
            mid = int((min_+max_)/2)
            no = self.find_no_pairs_less(mid,nums)
            if no >=k :
                max_ = mid
            else:
                min_ = mid+1
        return min_
