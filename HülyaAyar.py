import random

n = 1000
rand = [0]*n
interarrival_times = [0]*n
interarrival_times.append(0)
for i in range(n-1):
    rand[i] =  random.randint(1, 100)  
    if 1 <= rand[i] <= 12:
        interarrival_times[i]= 4
    elif 13 <= rand[i] <= 32:
        interarrival_times[i]= 8
    elif 33 <= rand[i] <= 56:
        interarrival_times[i]= 12
    elif 57 <= rand[i] <= 74:
        interarrival_times[i]= 16
    elif 75 <= rand[i] <= 90:
        interarrival_times[i]= 20
    elif 91 <= rand[i] <= 100:
        interarrival_times[i]= 24

rand2 = [0]*n
service_times = [0]*n
for k in range(n):
    rand2[k] =  random.randint(1, 100)  
    if 1 <= rand2[k] <= 50:
        service_times[k] =10
    elif 51 <= rand2[k] <= 75:
        service_times[k] =20
    elif 76<= rand2[k] <= 90:
        service_times[k] =15
    elif 91 <= rand2[k] <= 100:
        service_times[k] =5
        

time_service_begins = [0] * n
time_service_ends = [0] * n
idle_time = [0] * n
waiting_time_in_queue = [0] * n
time_customer_in_system = [0] * n

arrival_times = [0]* n#Calculating arrival times
sum = 0
for x in range(n):
    sum = sum + interarrival_times[x]
    arrival_times[x] = sum


#for first customer
time_service_begins[0]= interarrival_times[0]
time_service_ends[0] = time_service_begins[0] + service_times[0]
idle_time[0] = interarrival_times[0]
time_customer_in_system[0]=time_service_ends[0] - arrival_times[0]
waiting_time_in_queue[0]= time_service_begins[0] - arrival_times[0]


#for remaining customers
for i in range(1,n):
    idle_time[i] = arrival_times[i] - time_service_ends[i-1]
    if idle_time[i] < 0:
        idle_time[i] = 0
    time_service_begins[i] = max(interarrival_times[i], time_service_ends[i-1]) + idle_time[i]   
    time_service_ends[i] = time_service_begins[i] + service_times[i]
    waiting_time_in_queue[i] = time_service_begins[i] - arrival_times[i]
    time_customer_in_system[i] = time_service_ends[i]-arrival_times[i]
    
    
total_time_waiting = 0
for s in range(n):
    total_time_waiting = total_time_waiting + waiting_time_in_queue[s]
    
    
total_idle = 0
for e in range(n):
    total_idle = total_idle + idle_time[e]
    
    
    
for g in range(20):
    print("vehicle ",g)
    print("Interarrival Times: ", interarrival_times[g])
    print("Service times:" , service_times[g])
    print("Arrival Times: ", arrival_times[g])
    print("Time Service Begins: ", time_service_begins[g])
    print("Time Service Ends: ", time_service_ends[g])
    print("idle: ", idle_time[g])
    print("Waiting Time In Queue: ", waiting_time_in_queue[g])
    print("Time Customer In System: ", time_customer_in_system[g])
    

print("Average waiting time: ", total_time_waiting/n)
print("Average idle time: ", total_idle/time_service_ends[-1])