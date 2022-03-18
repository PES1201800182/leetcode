class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        num_dict = defaultdict(lambda:set())
        visited =set()
        for i in range(len(nums)):
            num_dict[nums[i]].add(i)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                temp = [i, j]
                if (nums[i],nums[j]) in visited :
                    continue
                visited.add((nums[i],nums[j]))
                sum = nums[i]+nums[j]

                if -sum in num_dict:
                    for k in num_dict[-sum]:
                        if k not in temp:
                            temp.append(k)
                            break
                if len(temp)==3:
                    temp = [nums[i] for i in temp]
                    ans.add(tuple(sorted(temp)))
        # ans=list(ans)
        # for i in range(len(ans)):
        #     ans[i]=list(ans[i])
        return ans
