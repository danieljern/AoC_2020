import time

def main():
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    sum_counts1, sum_counts2 = get_sum_counts("input.txt", alphabet)
    print(f"Part 1: The sum of counts = {sum_counts1}")
    print(f"Part 2: The sum of counts = {sum_counts2}")


def get_sum_counts(inputfile, key_set):
    groups1 = {}
    groups2 = {}
    row = 1
    count1 = 0
    count2 = 0
    for line in open(inputfile).read().split("\n"):
        if line != '':
            if "group" + str(row) in groups1:
                groups1["group" + str(row)].extend(line)
            else:
                groups1["group" + str(row)] = list(set(line))
            if "group" + str(row) in groups2:
                groups2["group" + str(row)].append(set(line))
            else:
                groups2["group" + str(row)] = [set(line)]
        else:
            row += 1
    # print(f"groups1: {groups1}")
    # print(f"groups2: {groups2}")
    for group1 in groups1:
        count1 += len(set(groups1[group1]).intersection(key_set))
    for group2 in groups2:
        if len(groups2[group2]) > 1:
            count2 += len(set.intersection(*groups2[group2]))
        else:
            count2 += len(groups2[group2][0])
    return count1, count2


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s milliseconds ---" % (1000*(time.time() - start_time)))