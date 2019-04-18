"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2015-02-10
-------------------------------------------------------
"""
import random
from Patron import Patron
from Server import Server
from queue_array import Queue

print("Welcome to the Dew-Drop Inn. Party Hearty - but Responsibly!")
print()
print("Please enter the following parameters:")
run_time = int(input("    Run time (minutes): "))
number_servers = int(input("    Number of servers: "))
patrons_per_min = int(input("    Maximum number of patrons arriving per minute: "))
min_service_time = int(input("    Minimum service time (minutes): "))
max_service_time = int(input("    Maximum service time (minutes): "))
chance_of_rejection = float(input("    Chance of a patron being rejected: "))

q = Queue()
servers = []
patron_count = 0
average_service_time = 0
past_queue_size = len(q)
total_wait_time = 0
total_wait_time_left_over = 0
idle_time = 0
rejection = 0
for x in range(number_servers+1):
    s = Server(x+1, None)
    servers.append(s)
for i in range(run_time):
    if past_queue_size < len(q):
        past_queue_size = len(q)
    print("Time {}".format(i))
    number_patrons = random.randint(0, patrons_per_min) 
    for y in range(number_patrons):
        print("Patron {} joins the queue.".format(int(str(y+1)+str(i))))
        service_length = random.randint(min_service_time, max_service_time)
        average_service_time += service_length
        p = Patron(int(str(y+1)+str(i)), i, service_length, chance_of_rejection)
        q.insert(p)
        patron_count += 1
    for z in range(len(servers)-1):
        if servers[z].is_serving() == False:
            if len(q) != 0:
                next_patron = q.remove()
                total_wait_time += (i-next_patron.arrival_time)
                rejection += servers[z].serving(i, next_patron)
                print("Server {} is now serving Patron {}".format(servers[z].number, next_patron.number))
            else:
                idle_time += 1
        else:
            servers[z].serving(i, next_patron)
    if i == (run_time-1):
        left_over = len(q)
        for a in range(len(q)):
            next_patron = q.remove()
            total_wait_time_left_over += (i-next_patron.arrival_time)
            
patron_count -= left_over
average_service_time = average_service_time/patron_count
ratio = idle_time/total_wait_time
total_wait_time = total_wait_time/patron_count
total_wait_time_left_over = total_wait_time_left_over/left_over
print("")
print("The number of patrons served: {}".format(patron_count))
print("The number of patrons rejected: {}".format(rejection))
print("Average service time per patron (minutes): {:.2f}".format(average_service_time))
print("The maximum queue size: {}".format(past_queue_size))
print("The number of patrons left in the queue: {}".format(left_over))
print("The average wait time in the queue for patrons allowed in (minutes): {:.2f}".format(total_wait_time))
print("The average wait time in the queue for patrons left over (minutes): {:.2f}".format(total_wait_time_left_over))
print("The average idle time per server (minutes): {}".format(idle_time))
print("Ratio of average idle time to average wait time: {}".format(idle_time))