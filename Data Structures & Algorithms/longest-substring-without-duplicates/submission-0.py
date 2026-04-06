class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring = 0
        left = 0
        last_seen = {} 
    
        for right in range(len(s)):
            
            if s[right] in last_seen and last_seen[s[right]] >= left:
                left = last_seen[s[right]] + 1
                
            last_seen[s[right]] = right
            
            current_window_size = right - left + 1
            if max_substring < current_window_size:
                max_substring = current_window_size
                
        return max_substring