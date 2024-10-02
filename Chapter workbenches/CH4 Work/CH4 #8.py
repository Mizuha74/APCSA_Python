total_length = 0
word_count = 0

while True:
    word = input("enter a word (or press enter to finish): ")
    if word == "":
        break 
    total_length += len(word)
    word_count += 1


if word_count > 0:
    average_length = round(total_length / word_count)
    print(f"Average word length: {average_length}")
else:
    print("No words were entered.")
