s =  input("Enter the string: ")
vowels = set("aeiou")
count = 0

for i in s:
    if i in vowels:
        count += 1

print("Number of vowels:", count)