def first_recurring_char(s):
    for i in range(len(s)):
        if s[i] in s[i+1:]:
            return s[i]
    return None

# Contoh
print(first_recurring_char("abcaed"))