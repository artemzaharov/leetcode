from typing import List 


class Solution:
    """ Можно сделать в одном цикле то есть немного упростить но  сложность не поменяется"""
    def two_sum(self, nums, target):
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        print(hashmap)
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashmap:
                return [hashmap[difference], i]
        
        return []

n = [1, 4, 6, 5]
t = 9

print(Solution().two_sum(n, t))