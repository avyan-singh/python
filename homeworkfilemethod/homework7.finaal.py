import string
def ispangram(a):
    return set(string.ascii_lowercase).issubset(set(a.lower()))
print(ispangram("The quick brown fox jumps over the lazy dog"))
    