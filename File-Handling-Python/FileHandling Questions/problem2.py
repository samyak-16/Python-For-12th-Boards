# Write a program to:

# Read a file data.txt
# Display all lines that start with a vowel


with open("data.txt", "r") as f:
    for line in f:
        vowels = ["a", "e", "i", "o", "u"]
        if line[0].lower() in vowels:
            print(line)
