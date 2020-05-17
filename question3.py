print("Enter string: ")
st = input()
a = ""
for k in range(0, len(st)):
    if st[k] == " ":
        a = a + " "
    elif st[k] not in a:
        a = a + st[k]
print("String after removing duplicate letters: ", a)

# Code by shreyansh sharma