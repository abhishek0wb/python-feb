items = ["apple", "banana", "arange", "apple", "mango"]

unique = set()

for item in items:
    if item in unique:
        print("duplicate: ",item)
        break
    unique.add(item)