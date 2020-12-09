import time
import re

def main():
    my_color = "shiny gold"
    bag_rules = get_rules("input.txt")
    print(bag_rules)
    my_count1 = 0
    my_count2 = 0
    for color in bag_rules:
        if color != my_color:
            my_count1 += count_bags_part1(bag_rules, my_color, color)
            # print(f"my_count_main = {my_count}")
    print(f"Part 1: Bag colors that contain at least one shiny gold bag = {my_count1}")
    for color, value in bag_rules[my_color].items():
        my_count2 += int(value) * count_bags_part2(bag_rules, color)
        # print(f"my_count2 in main: {my_count2}")
    print(f"Part 2: One single shiny gold bag contains: {my_count2} bags")


def get_rules(inputfile):
    rules = {}
    for line in open(inputfile).read().split("\n"):
        temp_bag = re.findall(r"(.*) bags contain", line)[0]
        bags_in_bag = re.findall(r"bags contain (.*)", line)[0].replace(".","").split(", ")
        if bags_in_bag[0] != "no other bags":
            for n in range(len(bags_in_bag)):
                n_bag_color = re.findall(r"[0-9] (.*) bag", bags_in_bag[n])[0]
                n_bag_quantity = re.findall(r"[0-9]", bags_in_bag[n])[0]
                if temp_bag in rules:
                    rules[temp_bag].update({n_bag_color: n_bag_quantity})
                else:
                    rules[temp_bag] = {n_bag_color: n_bag_quantity}
        else:
            rules[temp_bag] = {"other": "no"}
    return rules


def count_bags_part1(bags, color, curr_bag):
    # print(f"curr_bag: {curr_bag}")
    if curr_bag == color:
        # print("curr_bag == color")
        return 1
    elif bags.get(curr_bag) == None:
        # print("bags.get(curr_bag) == None")
        return 0
    else:
        my_count = []
        for key in bags[curr_bag]:
            my_count.append(count_bags_part1(bags, color, key))
            # print(f"my_count: {my_count}")
        return max(my_count)


def count_bags_part2(bags, curr_color):
    my_count = 0
    if "no" in bags[curr_color].values():
        return 1
    else:
        for bag_color, bag_value in bags[curr_color].items():
            # print(f"{curr_color} contain {bag_value} {bag_color}")
            my_count += int(bag_value) * count_bags_part2(bags, bag_color)
            # print(f"my_count: {my_count}")
        return my_count + 1


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))