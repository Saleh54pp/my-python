num = input("number?")

max_digit = 0

for ch in num:
    if ch.isdigit():
        d = int(ch)
        if d > max_digit:
            max_digit = d

print(" max digit in muber is: =", max_digit)
