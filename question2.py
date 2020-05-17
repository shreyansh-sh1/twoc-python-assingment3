# permutation of string
def toString(List):
    return ''.join(List)

def permute(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]

print("Enter string to find its permutations: ")
st = input()
l = len(st)
a = list(st)
print("all the possible permutations are")
permute(a, 0, l - 1)

# Code by shreyansh sharma