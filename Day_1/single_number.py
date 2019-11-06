# My solution
import math
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        else: 
            nums.sort()
            for i in range(1,len(nums)):
                if nums[i-1] == nums[i]:
                    nums[i-1] = math.inf
                    nums[i] = math.inf
            nums.sort()
            return nums[0]

# Solution 2

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]
"""
Complexity Analysis

Time complexity : O(n.1) = O(n). Time complexity of for loop is O(n). Time complexity of hash table(dictionary in python) operation pop is O(1).

Space complexity : O(n). The space required by hash_table is equal to the number of elements in nums.
"""

# Solution 3 (Fastest)

"""
Bit Manipulation
Concept

If we take XOR of zero and some bit, it will return that bit
a \oplus 0 = aa⊕0=a
If we take XOR of two same bits, it will return 0
a \oplus a = 0a⊕a=0
a \oplus b \oplus a = (a \oplus a) \oplus b = 0 \oplus b = ba⊕b⊕a=(a⊕a)⊕b=0⊕b=b
So we can XOR all bits together to find the unique number.

Just remembe the properties of XOR
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a
