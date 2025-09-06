Mode = int(input("Enter the Unit (1=km/hr , 2=m/s): "))
Distance = int(input("Enter the distance in kilometers: "))
time = int(input("Enter the time in hours: "))
velocity = Distance / time

if Mode == 1:
    print(int(velocity), "km/h")
elif Mode == 2:
    velocity = velocity * 0.277777778
    print(int(velocity), "m/s")
else:
    print("Invalid mode selected.")
