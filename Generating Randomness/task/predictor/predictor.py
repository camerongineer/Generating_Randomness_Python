char_array = []
while len(char_array) < 100:
    print("Print a random string containing 0 or 1:\n")
    string = input()
    for char in string:
        if char == "0" or char == "1":
            char_array.append(char)
    if len(char_array) < 100:
        print(f"Current data length is {len(char_array)}, {100 - len(char_array)} symbols left")

print("\nFinal data string:\n" + "".join(char_array))
