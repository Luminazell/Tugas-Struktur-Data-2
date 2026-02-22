from collections import OrderedDict

def deduplikasi(lst):
    return list(OrderedDict.fromkeys(lst))

# Contoh
data = [1, 2, 2, 3, 4, 3, 5]
print(deduplikasi(data))