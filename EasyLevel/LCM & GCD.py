
names = []
print("Enter names, type 'done' when finished:")

while True:
    name = input()
    if name.lower() == 'done':
        break
    names.append(name)
order = input("Order (A/D): ").upper()

if order == 'A':
    names.sort()  
elif order == 'D':
    names.sort(reverse=True)  
print("Sorted list:")
for name in names:
    print(name)
