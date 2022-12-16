def collect_user_input() -> str:
    char_array = []
    while len(char_array) < 100:
        print("Print a random string containing 0 or 1:\n")
        string = input()
        for char in string:
            if char == "0" or char == "1":
                char_array.append(char)
        if len(char_array) < 100:
            print(f"Current data length is {len(char_array)}, {100 - len(char_array)} symbols left")
    final_data_string = "".join(char_array)
    print(f"\nFinal data string:\n{final_data_string}\n")
    return final_data_string


def triad_evaluation(final_data_string: str):
    triad_map = {"000": [0, 0],
                 "001": [0, 0],
                 "010": [0, 0],
                 "011": [0, 0],
                 "100": [0, 0],
                 "101": [0, 0],
                 "110": [0, 0],
                 "111": [0, 0]}
    for i in range(3, len(final_data_string)):
        triad = final_data_string[i - 3] + final_data_string[i - 2] + final_data_string[i - 1]
        if final_data_string[i] == "0":
            triad_map[triad][0] += 1
        else:
            triad_map[triad][1] += 1
    for element in triad_map:
        print(f"{element}: {triad_map[element][0]},{triad_map[element][1]}")


triad_evaluation(collect_user_input())
