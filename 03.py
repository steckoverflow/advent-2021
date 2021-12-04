# 3-1
with open("input3-1-lange.txt", "r") as f:
    data = [r.replace("\n","") for r in f.readlines()]

gamma_rate_str = epsilon_rate_str = b""

# i pos of binary rep
for i in range(len(data[0])):
    # if sum of all ones are more than the length of all values 
    if sum([int(r[i:i+1]) for r in data]) > (len(data)//2):
        gamma_rate_str += b"1"
        epsilon_rate_str += b"0"
    else:
        gamma_rate_str += b"0"
        epsilon_rate_str += b"1"

print("Result 1:", int(gamma_rate_str, 2) * int(epsilon_rate_str, 2))

#3-2
import math
oxy_data = co2_data = data

i = 0
while len(oxy_data) > 1:
    if sum([int(r[i:i+1]) for r in oxy_data]) >= (math.ceil(len(oxy_data)/2)):
        oxy_data = [v for v in oxy_data if v[i:i+1] == "1"]
    else:
        oxy_data = [v for v in oxy_data if v[i:i+1] == "0"]
    i += 1
    
    #print("Iteration: ", i, "Remainder: ", oxy_data)
    

i = 0
while len(co2_data) > 1:
    if sum([int(r[i:i+1]) for r in co2_data]) >= (math.ceil(len(co2_data)/2)):
        co2_data = [v for v in co2_data if v[i:i+1] == "0"]
    else:
        co2_data = [v for v in co2_data if v[i:i+1] == "1"]
    i += 1

print("Result 2:", oxy_data, co2_data, int(oxy_data[0], 2) * int(co2_data[0], 2))
