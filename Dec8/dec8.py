import time

def main():
    list_op = [{"operation": line.split(" ")[0], "value": int(line.split(" ")[1])} for line in open("input.txt").read().split("\n")]
    value1, terminated = get_last_value(list_op)
    print(f"Part 1: Before any instruction is executed a second time, accumulator = {value1}")
    n = 0
    while terminated == False:
        sequence_temp = []
        for index in range(len(list_op)):
            sequence_temp.append(list_op[index].copy())
        # print(f"n: {n}")
        if list_op[n]["operation"] == "jmp":
            sequence_temp[n]["operation"] = "nop"
            # print(f"jmp -> nop at {n}:{list_op[n]} -> {sequence_temp[n]}")
            value2, terminated = get_last_value(sequence_temp)
        elif list_op[n]["operation"] == "nop" and list_op[n]["value"]:
            sequence_temp[n]["operation"] = "jmp"
            # print(f"nop -> jmp at {n}:{list_op[n]} -> {sequence_temp[n]}")
            value2, terminated = get_last_value(sequence_temp)
        n += 1
    print(f"Part 2: When the program teriminates, accumulator = {value2}")


def get_last_value(sequence):
    terminated = False
    accumulator = 0
    n = 0
    index_list = []
    while (n not in index_list):
        # print(f"sequence[{n}] = {sequence[n]['operation']} {sequence[n]['value']}")
        if sequence[n]["operation"] == "nop":
            index_list.append(n)
            n += 1
        elif sequence[n]["operation"] == "acc":
            accumulator += sequence[n]["value"]
            index_list.append(n)
            n += 1
        elif sequence[n]["operation"] == "jmp":
            index_list.append(n)
            n += sequence[n]["value"]
        if n > len(sequence) - 1:
            terminated = True
            return accumulator, terminated
    # print(f"last n: {last_index}, n now: {n}")
    return accumulator, terminated


def get_last_value2(sequence):
    accumulator = 0
    n = 0
    last_index = 0
    index_list = []
    while (n < len(sequence)-1):
        print(f"length of sequence: {len(sequence)}     sequence[{n}] = {sequence[n]['operation']} {sequence[n]['value']}")
        if sequence[n]["operation"] == "nop":
            index_list.append(n)
            last_index = n
            n += 1
        elif sequence[n]["operation"] == "acc":
            accumulator += sequence[n]["value"]
            index_list.append(n)
            last_index = n
            n += 1
        elif sequence[n]["operation"] == "jmp":
            index_list.append(n)
            last_index = n
            n += sequence[n]["value"]
    print(f"last n: {last_index}, n now: {n}")
    return accumulator


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))