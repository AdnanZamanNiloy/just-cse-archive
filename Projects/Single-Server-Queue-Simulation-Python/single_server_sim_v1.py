import numpy as np

def interarrival_time():
    return np.random.randint(1, 6)  

def service_time():
    return np.random.randint(2, 5) 

time = 0
server_busy = False
queue = []
arrival_time_next = interarrival_time()
departure_time_next = float("inf")
delays = []
Ti = {}
last_event_time = 0
total_customers_served = 0

def update_Ti(current_time):
    global last_event_time
    q_len = len(queue)
    duration = current_time - last_event_time
    Ti[q_len] = Ti.get(q_len, 0) + duration
    last_event_time = current_time

t_max = 50

   
while time < t_max:
    next_time = min(arrival_time_next, departure_time_next, t_max)
    update_Ti(next_time)
    time = next_time

    if time == t_max:
        break


    if arrival_time_next == time:
        arrival_time_next = time + interarrival_time()
        if not server_busy:
            delays.append(0)
            server_busy = True
            departure_time_next = time + service_time()
        else:
            queue.append(time)

    else:
        total_customers_served += 1
        if len(queue) > 0:
            arrival_t = queue.pop(0)
            delay = time - arrival_t
            delays.append(delay)
            departure_time_next = time + service_time()
        else:
            server_busy = False
            departure_time_next = float("inf")


avg_wait = sum(delays) / len(delays)
print(f"Average waiting time in queue = {avg_wait:.2f}")

total_time = last_event_time
total = 0
for key, value in Ti.items():
    total += key * value
avg_q_len = total / total_time
print(f"Average queue length = {avg_q_len:.2f}")

print("\nCustomers served =", total_customers_served)

print("\nTi values:")
for key in sorted(Ti.keys()):
    print(f"T[{key}] = {Ti[key]}")
