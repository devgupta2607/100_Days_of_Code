#Solution 1
class Solution:
    def reverseString(self, s) :
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


# Solution 2
class Solution:
    def reverseString(self, s) :
        """
        Do not return anything, modify s in-place instead.
        """
        left,right = 0, len(s)-1
        while left < right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -=1
        return s

#Solution 3 (faster than the above and equal to Sol1)

class Solution:
    def reverseString(self, s) :
        """
        Do not return anything, modify s in-place instead.
        """
        left,right = 0, len(s)-1
        while left < int(len(s)/2):
            s[left],s[right] = s[right],s[left]
            left += 1
            right -=1
        return s
