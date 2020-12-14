import time
import math
import numpy as np

def main():
   data = [line for line in open("input.txt").read().split("\n")]
   buses = data[1].split(",")
   time_arrival = float(data[0])
   bus_table1 = [int(number) for number in list(filter(lambda x: x.isdigit(), [char for char in data[1].split(",")]))]
   time_bus, my_bus = get_next_bus(time_arrival, bus_table1)
   print(f"Part 1: Bus ID {my_bus} * {time_bus - int(time_arrival)} minutes to wait = {my_bus * (time_bus - int(time_arrival))} ")

   modulos = {}
   # Find all modulos for each bus in input, so that: Bus % Modulo = Remainder
   # Example: Buses = [7,13,x,x,59,x,31,19] (Remainder = [0,+1,-,-,+4,-,+6,+7])
   #          Modulos = [0,12,-,-,55,12]
   for n in range(len(buses)):
       if buses[n] != "x":
           modulos[int(buses[n])] = -n % int(buses[n])
   buses_sorted = list(reversed(sorted(modulos)))
   start_time = modulos[buses_sorted[0]]
   time_step = buses_sorted[0] # Use the largest time step
   for bus in buses_sorted[1:]:
       while start_time % bus != modulos[bus]:
           start_time += time_step
       # print(f"{start_time} % {bus} = {start_time % bus}")
       time_step *= bus
   print(f"Part 2: Start time for perfect offset matching = {start_time}")


def get_next_bus(my_time, time_table):
    time_min = 9999999999  # minimum time to wait
    bus_id = 0
    for bus in time_table:
        time_curr = math.ceil(my_time / bus) * bus
        if time_curr < time_min:
            time_min = time_curr
            bus_id = bus
    return time_min, bus_id


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))