# Write a program to:

# Read a text file story.txt
# Count and display the number of lines, words, and characters


with open("story.txt", "r") as f:
    lines_count = 0
    words_count = 0
    characters_count = 0

    for line in f:
        lines_count += 1
        words = line.split(" ")
        words_count += len(words)
        characters_count += len(line)

    print(lines_count)
    print(words_count)
    print(characters_count)
