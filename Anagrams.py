from collections import Counter

def is_anagram(str1, str2):
    # Standardize input: convert to lowercase and remove spaces
    clean_str1 = str1.replace(" ", "").lower()
    clean_str2 = str2.replace(" ", "").lower()
    
    # Compare character frequencies
    return Counter(clean_str1) == Counter(clean_str2)

# Test cases
print(is_anagram("Listen", "Silent"))  # Returns True
print(is_anagram("Hello", "World"))    # Returns False
