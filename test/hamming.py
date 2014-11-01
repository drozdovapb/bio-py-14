str1 = input()
str2 = input()

def hamming(str1, str2):
    if len(str1)==len(str2):
        distance = 0
        for l, r in zip(str1, str2):
            if l != r:
                distance += 1
        return distance
    return -1

print(hamming(str1, str2))


k = int(input())

def find_substrings(str1, str2, k):
    for i in range(len(str1)):
        if hamming(str1, str2[:i]) <= k:
            print(str2[:i])

print(find_substrings(str1, str2, k))
