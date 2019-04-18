"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2015-03-05
-------------------------------------------------------
"""

import processor
import random

number_processors = int(input("Number of processors: "))
thread_production_length = int(input("Length of Thread production: "))
min_thread_time = int(input("Minimum Thread execution time: "))
max_thread_time = int(input("Maximum Thread execution time: "))

print()
print("Starting Simulation")
print()
print("Simulation length: {}".format(thread_production_length))
print("Number of processors: {}".format(number_processors))
print("Minimum / Maximum thread time: {} / {}".format(min_thread_time, max_thread_time))

processors_list = []
deque_list = []
done = 0
time = 0
for i in range(number_processors):
    processors = processor.Processor(i)
    processors_list.append(processors)

while done != number_processors:
    print("----------------------------------------")
    done = 0
    print("Time = {}".format(time))
    if thread_production_length >= time and time >= 0:
        thread_time = random.randint(min_thread_time, max_thread_time)
        thread = processor.Thread(time, thread_time)
        random_processor = random.randint(0, number_processors-1)
        if processors_list[random_processor].thread == None:
            processors_list[random_processor].thread = thread
            print("Thread {} added to processor {}".format(processors_list[random_processor].thread.number, random_processor))
        else:
            processors_list[random_processor].deque.insert_front(processors_list[random_processor].thread)
            processors_list[random_processor].thread = thread
            print("Thread {} added to processor {}".format(processors_list[random_processor].thread.number, random_processor))
    for i in range(len(processors_list)):
        if processors_list[i].thread != None:
            if processors_list[i].thread.current_time == 0:
                print("Thread {} finished on processor {}".format(processors_list[i].thread.number, i))
                processors_list[i].thread = None
            else:
                processors_list[i].thread.current_time -= 1
                processors_list[i].working += 1
        else:
            if processors_list[i].deque.is_empty() == False:
                processors_list[i].thread = processors_list[i].deque.remove_front()
            else:
                random_processor = random.randint(0, number_processors-1)
                while random_processor == i:
                    random_processor = random.randint(0, number_processors-1)
                if processors_list[random_processor].deque.is_empty() == False:
                    processors_list[i].thread = processors_list[random_processor].deque.remove_rear()
                    print("Thread {} stolen from processor {} by processor {}".format(processors_list[i].thread.number, random_processor, i))
                else:
                    print("Processor {} fails to steal a process from processor {}".format(i, random_processor))
                    done += 1
    time += 1
print("----------------------------------------")
print("All processes finished")
print("----------------------------------------")
print("Statistics")
print()
for i in range(len(processors_list)):
    busy_percent = (processors_list[i].working/time)*100
    print("Processor {} was busy {:.2f}% of the time".format(i, busy_percent))