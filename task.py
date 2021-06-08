class Solution(object):

    def __init__(self, nums, k_value):
        self.result = self.checkSubarraySum(nums, k_value)

    def checkSubarraySum(self, nums, k_value):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if nums == None or len(nums) == 0 or len(nums) == 1:
            return False
        mapping, summary = {}, 0
        mapping[0] = 0

        for element in range(len(nums)):
            if k_value != 0:
                summary = (summary + nums[element]) % k_value
            else:
                summary = summary + nums[element]
            if summary in mapping:
                index = mapping[summary]
                if (element - index >= 1):
                    return True
                else:
                    continue
            else:
                mapping[summary] = element + 1
        return False

# test data from code description
nums_1, k1 = ([23,2,4,6,7], 6)
nums_2, k2 = ([23,2,6,4,7], 13)

test_true = Solution(nums_1,k1)
test_false = Solution(nums_2,k2)
# print results of task True / False scenarios
print(test_true.result)
print(test_false.result)