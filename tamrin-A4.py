text = input("  enter a string : ")

reverse_text = ""

index = len(text) - 1
while index >= 0:
    reverse_text += text[index]
    index -= 1

print(" revesrse text is =", reverse_text)
