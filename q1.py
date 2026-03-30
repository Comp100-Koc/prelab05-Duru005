def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    max_length = 0
    res = ""
    for i in range(len(s)):
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            
            if (right-left+1) > max_length:
                max_length = right-left+1
                res = s[left:right+1]
                
            left -= 1
            right +=1
        
        left, right = i, i+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            
            if (right-left+1) > max_length:
                max_length = right-left+1
                res = s[left:right+1]
                
            left -= 1
            right +=1
            
    if max_length < 2:
        return ""
    return res