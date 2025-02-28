light = input(" Enter Red or Green : ").strip().lower()
movement = input(" Do you want to move? (Yes / No ):  ").strip().lower()

if(light == "green" and movement == "yes"):
    print("You are safe to go now")

elif(light == "green" and movement == "no"):
    print("You are waisting your time")

elif ( light == "red" and movement == "no"):
    print("Clever Choice")

elif ( light == "red" and movement == "yes"):
    print("You are  Eleminated ! Game Over! ")

else: print("Enter  Valid Options")
