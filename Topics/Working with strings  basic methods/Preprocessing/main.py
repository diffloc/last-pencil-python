str_input = input()
punctuation = ",.!?"
for i in punctuation:
    str_input = str_input.replace(i, "")

str_input = str_input.lower()

print(str_input)
