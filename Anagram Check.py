def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# Contoh
print(is_anagram("listen", "silent"))