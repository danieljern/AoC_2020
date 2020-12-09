import time

def main():
    list_numbers = [int(line) for line in open("input.txt").read().split("\n")]
    pos = 25 # Length of preamble. 25 for input, always interested in the last value
    invalid_number, invalid_pos = get_invalid_value(list_numbers, pos)
    print(f"Part 1: Invalid number at pos {invalid_pos} = {invalid_number}")
    list_numbers2 = list_numbers[0:invalid_pos]
    contigious_set = get_contigious_set(list_numbers2, invalid_number)
    print(f"Part 2: Min value = {min(contigious_set)}, Max value = {max(contigious_set)}, Min + Max = {min(contigious_set) + max(contigious_set)}")


def get_invalid_value(numbers, offset):
    preamble_check = True
    n = 0
    while preamble_check == True:
        temp_number = numbers[n + offset]
        # print(f"n: {n}     pos + n: {pos + n}   temp_number: {temp_number}")
        preamble = numbers[n:n + offset]
        temp_compare = [temp_number - x for x in preamble]
        if set(preamble).intersection(temp_compare):
            preamble_check = True
            n += 1
        else:
            preamble_check = False
            invalid_number = temp_number
            invalid_pos = n + offset
    return invalid_number, invalid_pos


def get_contigious_set(numbers, number):
    cont_set = numbers[-2:]
    n = 3
    while sum(cont_set) != number:
        if sum(cont_set) > number:
            if n < len(numbers) - 1:
                cont_set.remove(cont_set[-1])
                cont_set.insert(0, numbers[-n])
                n += 1
            else:
                cont_set.remove(cont_set[0])
        elif sum(cont_set) < number:
            cont_set.insert(0, numbers[-n])
            n += 1
        # print(f"n = {n}    sum(cont_set) = {sum(cont_set)}  number = {number}")
    return cont_set


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))