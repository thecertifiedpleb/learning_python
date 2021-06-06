import time

########## VARIABLES ##########
weight = float(input("Weight of package: "))
ground_rate = 20
drone_rate = 0
ground_p_rate = 125
cheapest = ""

########## CALCULATION ##########

if weight <= 2:
  ground_rate += (weight * 1.5)
  drone_rate = (weight * 4.5)
elif weight <= 6:
  ground_rate += (weight * 3)
  drone_rate = (weight * 9)
elif weight <= 10:
  ground_rate += (weight * 4)
  drone_rate = (weight * 12)
elif weight > 10:
  ground_rate += (weight * 4.75)
  drone_rate = (weight * 14.25)
else:
  print("Please enter a valid weight.") 
  
ground_rate = round(ground_rate, 2)
ground_p_rate = round(ground_p_rate, 2)
drone_rate = round(drone_rate, 2)


print("\nTotal via Ground: $" + str(ground_rate))
print("Total via Ground Premium $" + str(ground_p_rate))
print("Total via Drone: $" + str(drone_rate))


########## COMPARE ##########

if ground_rate < ground_p_rate and ground_rate < drone_rate:
  cheapest = "Ground"
elif ground_p_rate < ground_rate and ground_p_rate < drone_rate:
  cheapest = "Ground Premium"
elif drone_rate < ground_rate and drone_rate < ground_p_rate:
  cheapest = "Drone"


print("\nWe recommend shipping via " + cheapest + ", as it will be your least expensive option.") 

#time.sleep(100)

