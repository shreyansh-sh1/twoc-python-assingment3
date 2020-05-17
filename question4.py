a=[]
b=[]
c=int(input("Enter number of items in list: "))
print("Enter items: ")
for i in range(c):
    d=input()
    a.append(d)
for j in range(len(a)):
    if a[j] not in b:
        b.append(a[j])
print("List after removed duplicate items: ",b)

# Code by shreyansh sharma