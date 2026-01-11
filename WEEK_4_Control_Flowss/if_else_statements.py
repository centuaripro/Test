

# Take input and validate to ensure its amongst allowed/permitted colours
light = input("What colour is the traffic light?")

# allowed colours red, yellow and green

if light == "red" or light == "yellow" or light == "green":
    


    if light == "green" or light == "blinking":
        print("Go")
    elif light == "yellow":
        print("Slow down")
    else:
        print("stop")
else:
    print("Valid colours are red, green and yellow ONLY")

# print("")
# print("-------------------------")
# print("")

# temperature = 35
# humidity = 15

# if temperature <= 10 or humidity <= 5:
#     print("Warning: Unusual weather condition detected")
# else:
#     print("Weather conditions are normal")
    
