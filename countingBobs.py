s =  input("Enter the string: ").lower()
print(s)
word = set("bob")
count = 0

for i in range(len(s)):
    if s[i:i+3] == "bob":
        count += 1
        continue
print("Number of times bob occurs is: ", count)