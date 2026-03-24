# Write a program to:

# Replace all occurrences of the word "old" with "new" in a file file.txt
updated_text = ""
with open("file.txt", "r+") as f:
    texts = f.read()
    updated_text = texts.replace("old", "new")

with open("file.txt", "w") as f:
    f.write(updated_text)
