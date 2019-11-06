#Solution 1
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        len_str = len(s)
        list_str = list(s)
        
        for i in range(0,len_str, 2*k):
            list_str[i:i+k] = reversed(list_str[i:i+k])
        return "".join(list_str)

