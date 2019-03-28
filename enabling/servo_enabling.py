from gpiozero import Servo

DIRECTION_SERVO_PIN = 2
directionServo = Servo(DIRECTION_SERVO_PIN)
directionServo.mid()

running = True
while running:
    response = input("Enter comand: ")
    if response.startswith("exit"):
        running = False
    else:
        try:
            value = float(response)
            directionServo.value = value
            print("Servo {}".format(value))
        except:
            print("Your expression doesn't match")

print("Closing application ...")
directionServo.detach()
exit(0)
