def interlace_strings(str1, str2):
    # Determine the length of the shorter string
    min_length = min(len(str1), len(str2))
    
    # Interlace the strings up to the length of the shorter string
    interlaced = ''.join([str1[i] + str2[i] for i in range(min_length)])
    
    # Append the remaining part of the longer string
    if len(str1) > len(str2):
        interlaced += str1[min_length:]
    else:
        interlaced += str2[min_length:]
    
    return interlaced

# Example usage
str1 = "abcdef"
str2 = "123"
result = interlace_strings(str1, str2)
print(result)  # Output: a1b2c3def