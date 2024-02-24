def washing_machine_time_estimate(weight):
    if 0 <= weight <= 7000:
        if weight == 0:
            return "Time Estimated: 0 Minutes"
        elif weight <= 2000:
            return "Time Estimated: 25 Minutes"
        elif 2001 <= weight <= 4000:
            return "Time Estimated: 35 Minutes"
        else:
            return "Time Estimated: 45 Minutes"
    else:
        return "INVALID INPUT"
weight_input = int(input("Enter the weight: "))
result = washing_machine_time_estimate(weight_input)
print(result)
