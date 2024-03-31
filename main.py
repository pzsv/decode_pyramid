def decode(message_file):
    file = open(message_file, "r")
    lines = file.readlines()
    dict = {}
    for line in lines:
        line_arr = line[:-1].split(" ")
        dict[int(line_arr[0])] = line_arr[1]

    sorted_keys = sorted(dict.keys())
    step = 1
    sequence = ""
    while len(sorted_keys) != 0:
        if len(sorted_keys) >= step:
            row = sorted_keys[0:step]
            sequence += dict.get(row[len(row)-1]) + " "
            sorted_keys = sorted_keys[step:]
            step += 1

    file.close()
    return sequence[:len(sequence)-1]

if __name__ == "__main__":
    print(decode("coding_qual_input.txt"))
