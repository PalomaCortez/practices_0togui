## C12 Tuples, sets and dictionaries
# EX5 - Count occurrence of words

def main():  # prompt the user to enter a file
    filename = input("Enter a filename: ").strip()
    infile = open(filename, "r")  # open the file

    word_counts = {}  # create na empty dictionary to count words
    for line in infile:
        process_line(line.lower(), word_counts)

    pairs = list(word_counts.items())  # get the pair of the dictionary

    items = [[x, y] for (y, x) in pairs]  # reserve pairs for the list

    items.sort()  # sort pairs in items

    for i in range(len(items) - 1, len(items) - 11, -1):
        print(items[i][1] + "\t" + str(items[i][0]))


# Count each word in the line
def process_line(line, word_counts):
    line = replace_punctuations(line)  # replace punctuations with space
    words = line.split()  # get words from each line
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1


# replace punctuation in line with a space
def replace_punctuations(line):
    for ch in line:
        if ch in "~@#$%ˆ&*()_+=~<>?/.,:;!{}[]|\"":
            line = line.replace(ch, " ")
    return line


main()
