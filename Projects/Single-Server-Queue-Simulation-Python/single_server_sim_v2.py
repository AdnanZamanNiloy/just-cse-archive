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
events = []

def update_Ti(current_time):
    global last_event_time
    q_len = len(queue)
    duration = current_time - last_event_time
    Ti[q_len] = Ti.get(q_len, 0) + duration
    last_event_time = current_time

for time in range(51):  
    update_Ti(time)
    
    event_occurred = False
    
    if time == arrival_time_next:
        events.append({"time": time, "event": "arrival", "queue_len": len(queue)})
        arrival_time_next = time + interarrival_time()
        event_occurred = True
        
        if not server_busy:
            delays.append(0)
            server_busy = True
            departure_time_next = time + service_time()
        else:
            queue.append(time)
    
    if time == departure_time_next:
        events.append({"time": time, "event": "departure", "queue_len": len(queue)})
        total_customers_served += 1
        event_occurred = True
        
        if len(queue) > 0:
            arrival_t = queue.pop(0)
            delay = time - arrival_t
            delays.append(delay)
            departure_time_next = time + service_time()  
        else:
            server_busy = False
            departure_time_next = float("inf")
    
    if not event_occurred:
        events.append({"time": time, "event": "Nothing happen", "queue_len": len(queue)})

update_Ti(50)

avg_wait = sum(delays) / len(delays)
print(f"Average waiting time in queue = {avg_wait:.2f}")

total_time = last_event_time
total = 0
for key, value in Ti.items():
    total += key * value
avg_q_len = total / total_time

print(f"Average queue length = {avg_q_len:.2f}")

print("\nCustomers served =", total_customers_served)

print("\nEvents:")
for event in events:
    print(event)
